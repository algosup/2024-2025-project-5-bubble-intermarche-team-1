import os
import csv
import pandas as pd
import ollama
import re

def load_wine_data(file_path):
    """
    Charge les données de vin à partir d'un fichier CSV
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Données chargées avec succès. {len(df)} vins trouvés.")
        return df
    except Exception as e:
        print(f"Erreur lors du chargement du fichier: {e}")
        return None

def generate_wine_description(wine_name, language):
    """
    Génère une description de vin en utilisant Ollama avec deepseek
    """
    if language == "français":
        prompt = f"""Je suis un expert en œnologie. Je dois écrire une description commerciale attrayante et détaillée pour le vin suivant : {wine_name}.
        
        Ma description doit:
        - Être écrite en français
        - Faire entre 1 et 2 phrases
        - Utiliser un vocabulaire riche et évocateur
        - Inclure des suggestions d'accords mets-vins si possible
        - Éviter les clichés tout en restant engageante"""
        
    else:  # English
        prompt = f"""I am a wine expert. I need to write an appealing and detailed commercial description for the following wine: {wine_name}.
        
        My description should:
        - Be written in English
        - Be 1 to 2 sentences long
        - Use rich and evocative vocabulary
        - Include food pairing suggestions if possible
        - Avoid clichés while remaining engaging"""

    try:
        response = ollama.chat(model='deepseek-r1:14b', messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ])
        
        # Extraire uniquement la réponse finale en supprimant la partie <think>...</think>
        content = response['message']['content']
        cleaned_content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()
        
        print(f"Prompt envoyé: {prompt}")
        print(f"Réponse nettoyée: {cleaned_content}")
        
        return cleaned_content
    except Exception as e:
        print(f"Erreur lors de la génération de la description: {e}")
        return f"Erreur: Impossible de générer une description pour {wine_name}"

def generate_wine_subcategories(wine_name, description_fr="", description_en=""):
    """
    Génère les sous-catégories d'un vin en utilisant Ollama
    """
    valid_categories = ["Red", "White", "Rosé", "Sparkling", "Light-bodied", "Medium-bodied", "Full-bodied"]
    categories_str = ", ".join(valid_categories)
    
    # Construire le prompt avec les informations disponibles
    prompt = f"""Je suis un expert en œnologie. Basé sur les informations suivantes sur un vin, je dois déterminer ses sous-catégories.

Nom du vin: {wine_name}
"""

    if description_fr and description_fr != "":
        prompt += f"Description française: {description_fr}\n"
    
    if description_en and description_en != "":
        prompt += f"Description anglaise: {description_en}\n"
    
    prompt += f"""
Parmi les catégories suivantes: {categories_str}
Sélectionne UNIQUEMENT les catégories qui correspondent à ce vin. 

Règles:
1. Chaque vin doit avoir au moins une catégorie de type (Red, White, Rosé ou Sparkling)
2. Chaque vin doit avoir au moins une catégorie de corps (Light-bodied, Medium-bodied ou Full-bodied)
3. Renvoie ta réponse sous forme de liste Python, par exemple: ["Red", "Full-bodied"]
4. N'inclus PAS d'explications, UNIQUEMENT la liste des catégories

Réponse:"""

    try:
        response = ollama.chat(model='deepseek-r1:14b', messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ])
        
        # Extraire uniquement la réponse finale en supprimant la partie <think>...</think>
        content = response['message']['content']
        cleaned_content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()
        
        print(f"Prompt envoyé pour les sous-catégories")
        print(f"Réponse nettoyée: {cleaned_content}")
        
        # Essayer d'extraire la liste
        try:
            # Chercher une liste dans le texte avec une regex
            list_match = re.search(r'\[.*?\]', cleaned_content)
            if list_match:
                list_str = list_match.group(0)
                # Évaluer la chaîne comme code Python
                import ast
                categories_list = ast.literal_eval(list_str)
                # Vérifier que ce sont des catégories valides
                validated_categories = [cat for cat in categories_list if cat in valid_categories]
                return validated_categories
            else:
                # Analyser manuellement si pas de liste trouvée
                categories_list = []
                for category in valid_categories:
                    if category.lower() in cleaned_content.lower():
                        categories_list.append(category)
                # Assurer qu'il y a au moins une catégorie de type et une de corps
                has_type = any(cat in categories_list for cat in ["Red", "White", "Rosé", "Sparkling"])
                has_body = any(cat in categories_list for cat in ["Light-bodied", "Medium-bodied", "Full-bodied"])
                
                if not has_type:
                    if "rouge" in cleaned_content.lower() or "red" in cleaned_content.lower():
                        categories_list.append("Red")
                    elif "blanc" in cleaned_content.lower() or "white" in cleaned_content.lower():
                        categories_list.append("White")
                    elif "rosé" in cleaned_content.lower() or "rose" in cleaned_content.lower():
                        categories_list.append("Rosé")
                    elif "pétillant" in cleaned_content.lower() or "sparkling" in cleaned_content.lower():
                        categories_list.append("Sparkling")
                    else:
                        categories_list.append("Red")  # Par défaut
                
                if not has_body:
                    if "léger" in cleaned_content.lower() or "light" in cleaned_content.lower():
                        categories_list.append("Light-bodied")
                    elif "corsé" in cleaned_content.lower() or "full" in cleaned_content.lower():
                        categories_list.append("Full-bodied")
                    else:
                        categories_list.append("Medium-bodied")  # Par défaut
                
                return categories_list
        except:
            # En cas d'erreur, valeurs par défaut
            return ["Red", "Medium-bodied"]
            
    except Exception as e:
        print(f"Erreur lors de la génération des sous-catégories: {e}")
        return ["Red", "Medium-bodied"]  # Valeurs par défaut en cas d'erreur

def process_wines(input_file, output_file):
    """
    Traite tous les vins dans le fichier d'entrée et écrit les résultats dans le fichier de sortie
    """
    df = load_wine_data(input_file)
    if df is None:
        return
    
    # Créer une copie du DataFrame pour éviter de modifier l'original
    result_df = df.copy()
    
    # Pour chaque vin, générer les descriptions et sous-catégories
    for index, row in df.iterrows():
        wine_name = row['name']
        if pd.isna(wine_name) or wine_name == "":
            continue
            
        print(f"\nTraitement du vin: {wine_name}")
        
        # Générer la description en français
        if pd.isna(row.get('descriptionFr', '')) or row.get('descriptionFr', '') == "":
            fr_description = generate_wine_description(wine_name, "français")
            result_df.at[index, 'descriptionFr'] = fr_description
            print(f"Description FR générée")
        else:
            fr_description = row['descriptionFr']
        
        # Générer la description en anglais
        if pd.isna(row.get('descriptionEn', '')) or row.get('descriptionEn', '') == "":
            en_description = generate_wine_description(wine_name, "english")
            result_df.at[index, 'descriptionEn'] = en_description
            print(f"Description EN générée")
        else:
            en_description = row['descriptionEn']
        
        # Générer les sous-catégories
        subcategories = generate_wine_subcategories(wine_name, fr_description, en_description)
        result_df.at[index, 'subCategories'] = str(subcategories).replace("'", '"')
        print(f"Sous-catégories générées: {subcategories}")
        
    # Enregistrer les résultats
    result_df.to_csv(output_file, index=False)
    print(f"\nTraitement terminé. Résultats enregistrés dans {output_file}")

if __name__ == "__main__":
    # Fichiers d'entrée et de sortie
    input_file = input("Entrez le chemin du fichier CSV contenant les vins: ")
    output_file = input("Entrez le chemin du fichier de sortie CSV: ")
    
    process_wines(input_file, output_file)