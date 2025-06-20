import csv
import os
import sys

def create_html_gallery(csv_file, output_html="gallery.html"):
    products = []

    # Check if the file exists
    if not os.path.exists(csv_file):
        print(f"Error: The file {csv_file} does not exist.")
        return False

    # Read the CSV file
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)  # Read the header

            # Check if the header is correct
            if header and len(header) >= 2 and header[0].lower() == "nom" and header[1].lower() == "lien":
                for row in reader:
                    if len(row) >= 2:
                        name = row[0].strip()
                        image_url = row[1].strip()
                        if name and image_url:  # Ignore rows with empty values
                            products.append({"name": name, "image_url": image_url})
            else:
                print("Error: The CSV format must have a header 'Nom,Lien'")
                return False
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return False

    if not products:
        print("No products with images were found in the file.")
        return False

    # Create the HTML content
    html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cheese Products Gallery</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .product {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            overflow: hidden;
            transition: transform 0.3s;
            text-align: center;
            padding-bottom: 15px;
        }
        .product:hover {
            transform: translateY(-5px);
        }
        .product img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            display: block;
        }
        .product-name {
            margin: 15px 10px 5px;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Cheese Products Gallery</h1>
    <div class="gallery">
"""

    # Add each product to the gallery
    for product in products:
        html_content += f"""        <div class="product">
            <img src="{product['image_url']}" alt="{product['name']}" onerror="this.src='https://via.placeholder.com/250x200?text=Image+not+available'; this.onerror=null;">
            <p class="product-name">{product['name']}</p>
        </div>
"""

    # Close the HTML tags
    html_content += """    </div>
</body>
</html>
"""

    # Write the HTML file
    try:
        with open(output_html, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"HTML gallery created successfully: {output_html}")
        return True
    except Exception as e:
        print(f"Error writing the HTML file: {e}")
        return False

def main():
    # Check arguments or use default values
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    else:
        csv_file = input("Enter the name of the CSV file (default: produits_avec_images.csv): ") or "produits_avec_images.csv"

    if len(sys.argv) > 2:
        output_html = sys.argv[2]
    else:
        output_html = input("Enter the name of the HTML file to create (default: gallery.html): ") or "gallery.html"

    create_html_gallery(csv_file, output_html)

if __name__ == "__main__":
    main()
