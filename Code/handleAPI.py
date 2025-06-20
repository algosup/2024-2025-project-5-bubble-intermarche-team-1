import csv
import os
import time
import requests

# Retrieve API keys from environment variables
API_KEY = os.getenv("GOOGLE_API_KEY")
CSE_ID = os.getenv("GOOGLE_CSE_ID")

def get_image_url(product):
    base_url = "https://www.googleapis.com/customsearch/v1"

    # Simple search parameters
    params = {
        'q': f"wines {product}",
        'cx': CSE_ID,
        'key': API_KEY,
        'searchType': 'image',
        'num': 1  # Just the first image
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Retrieve the image URL if available
        if 'items' in data and len(data['items']) > 0:
            return data['items'][0]['link']
        return ""
    except Exception:
        return ""

def main():
    # Check if API keys are available
    if not API_KEY or not CSE_ID:
        print("Error: Environment variables GOOGLE_API_KEY and GOOGLE_CSE_ID must be set")
        return

    input_file = "produits.csv"
    output_file = "produits_avec_images.csv"

    # Ask for filenames if necessary
    if not os.path.exists(input_file):
        input_file = input("Enter the name of the input CSV file: ")

    # Read the input file
    products = []
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0].strip():  # Ignore empty lines
                    products.append(row[0].strip())
    except Exception as e:
        # If the file is not a valid CSV, try to read it as a text file
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                products = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"Error reading the file: {e}")
            return

    if not products:
        print("No products found in the file.")
        return

    print(f"Processing {len(products)} products...")

    # Write the output file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Link"])  # Headers

        for i, product in enumerate(products):
            image_url = get_image_url(product)
            writer.writerow([product, image_url])
            print(f"Processing {product} ({i+1}/{len(products)}): {image_url}")

            # Pause to respect API limits
            if i < len(products) - 1:
                time.sleep(0.5)

    print(f"Done! Results saved in {output_file}")

if __name__ == "__main__":
    main()
