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
    Génère une description de vin en utilisant Mistral AI
    """
    if language == "français":
        prompt = f"""Je suis un expert en œnologie. Je dois écrire une description commerciale attrayante et détaillée pour le vin suivant : {wine_name}.
        
        Ma description doit:
        - Être écrite en français
        - Faire entre 10 et 20 mots
        - Utiliser un vocabulaire riche et évocateur
        - Inclure des suggestions d'accords mets-vins si possible
        - Éviter les clichés tout en restant engageante"""
        
    else:  # English
        prompt = f"""I am a wine expert. I need to write an appealing and detailed commercial description for the following wine: {wine_name}.
        
        My description should:
        - Be written in English
        - Be betwen 10 and 20 words
        - Use rich and evocative vocabulary
        - Include food pairing suggestions if possible
        - Avoid clichés while remaining engaging"""

    
    response = ollama.chat(model='deepseek-r1:14b', messages=[
        {
            "role": "user",
            "content": prompt,
        },
    ])

    # Récupérer le contenu de la réponse
    content = response['message']['content']

    # Filtrer la partie <think>...</think> en utilisant une expression régulière
    cleaned_content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()

    print(f"Prompt envoyé: {prompt}")
    print(f"Réponse reçue: {cleaned_content}")
    
    return cleaned_content
    

def process_wines(input_file, output_file):
    """
    Traite tous les vins dans le fichier d'entrée et écrit les résultats dans le fichier de sortie
    """
    df = load_wine_data(input_file)
    if df is None:
        return
    
    # Créer une copie du DataFrame pour éviter de modifier l'original
    result_df = df.copy()
    
    # Pour chaque vin, générer les descriptions
    for index, row in df.iterrows():
        wine_name = row['name']
        if pd.isna(wine_name) or wine_name == "":
            continue
            
        print(f"Traitement du vin: {wine_name} ({index + 1}/{len(df)})")
        
        # Générer la description en français
        if pd.isna(row['descriptionFr']) or row['descriptionFr'] == "":
            fr_description = generate_wine_description(wine_name, "français")
            result_df.at[index, 'descriptionFr'] = fr_description
            print(f"Description FR générée")
        
        # Générer la description en anglais
        if pd.isna(row['descriptionEn']) or row['descriptionEn'] == "":
            en_description = generate_wine_description(wine_name, "english")
            result_df.at[index, 'descriptionEn'] = en_description
            print(f"Description EN générée")
        
    # Enregistrer les résultats
    result_df.to_csv(output_file, index=False)
    print(f"Traitement terminé. Résultats enregistrés dans {output_file}")

if __name__ == "__main__":
    # Fichiers d'entrée et de sortie
    input_file = input("Entrez le chemin du fichier CSV contenant les vins: ")
    output_file = input("Entrez le chemin du fichier de sortie CSV: ")
    
    process_wines(input_file, output_file)