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

def generate_wine_subcategories(wine_name, description_fr="", description_en=""):
    """
    Génère les sous-catégories d'un fromage en utilisant Ollama
    """
    valid_categories = [
        "Soft & creamy", "Semi-soft", "Firm & hard", "Blue",
        "Cow", "Goat", "Sheep", "Mixed",
        "Mild", "Medium", "Strong", "Very strong"
    ]
    categories_str = ", ".join(valid_categories)
    
    # Construire le prompt avec les informations disponibles
    prompt = f"""Je suis un expert en fromages. Basé sur les informations suivantes sur un fromage, je dois déterminer ses sous-catégories.

Nom du fromage: {wine_name}
"""

    if description_fr and description_fr != "":
        prompt += f"Description française: {description_fr}\n"
    
    if description_en and description_en != "":
        prompt += f"Description anglaise: {description_en}\n"
    
    prompt += f"""
Parmi les catégories suivantes: {categories_str}
Sélectionne UNIQUEMENT les catégories qui correspondent à ce fromage. 

Règles:
1. Chaque fromage doit avoir au moins une catégorie de texture (Soft & creamy, Semi-soft, Firm & hard, Blue)
2. Chaque fromage doit avoir au moins une catégorie de lait (Cow, Goat, Sheep ou Mixed)
3. Chaque fromage doit avoir au moins une intensité (Mild, Medium, Strong, Very strong)
4. Renvoie ta réponse sous forme de liste Python, par exemple: ["Cow", "Firm & hard", "Strong"]
5. N'inclus PAS d'explications, UNIQUEMENT la liste des catégories

Réponse:"""

    try:
        response = ollama.chat(model='deepseek-r1:14b', messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ])
        
        content = response['message']['content']
        cleaned_content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()
        
        print(f"Prompt envoyé pour les sous-catégories")
        print(f"Réponse nettoyée: {cleaned_content}")
        
        try:
            list_match = re.search(r'\[.*?\]', cleaned_content)
            if list_match:
                list_str = list_match.group(0)
                import ast
                categories_list = ast.literal_eval(list_str)
                validated_categories = [cat for cat in categories_list if cat in valid_categories]
                return validated_categories
            else:
                categories_list = []
                for category in valid_categories:
                    if category.lower() in cleaned_content.lower():
                        categories_list.append(category)

                # Validation des trois axes
                has_texture = any(cat in categories_list for cat in ["Soft & creamy", "Semi-soft", "Firm & hard", "Blue"])
                has_milk = any(cat in categories_list for cat in ["Cow", "Goat", "Sheep", "Mixed"])
                has_intensity = any(cat in categories_list for cat in ["Mild", "Medium", "Strong", "Very strong"])
                
                if not has_texture:
                    categories_list.append("Semi-soft")
                if not has_milk:
                    categories_list.append("Cow")
                if not has_intensity:
                    categories_list.append("Medium")
                
                return categories_list
        except:
            return ["Cow", "Semi-soft", "Medium"]
            
    except Exception as e:
        print(f"Erreur lors de la génération des sous-catégories: {e}")
        return ["Cow", "Semi-soft", "Medium"]


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
        
        # Recup la description en français
        if pd.isna(row.get('descriptionFr', '')) or row.get('descriptionFr', '') == "":
            result_df.at[index, 'descriptionFr'] = fr_description
        else:
            fr_description = row['descriptionFr']
        
        # Recup la description en anglais
        if pd.isna(row.get('descriptionEn', '')) or row.get('descriptionEn', '') == "":
            result_df.at[index, 'descriptionEn'] = en_description
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