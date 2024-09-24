import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de base pour les recherches d'iPhone 15 Pro Max sur Jumia
url = "https://www.jumia.ma/catalog/?q=iphone+15+pro+max&page="

# Dictionnaire pour stocker les noms, prix et anciens prix
columns = {'name': [], 'price': [], 'old_price': []}

# Boucle sur les pages (de 1 à 9)
for page in range(1, 10):
    print('--- Page', page, '---')
    # Requête GET pour récupérer le contenu HTML de chaque page
    r = requests.get(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")

    # Trouver tous les articles de produits sur la page
    articles = soup.find_all('article', {'class': 'prd _fb col c-prd'})
    
    # Extraire le nom, le prix et l'ancien prix pour chaque produit
    for article in articles:
        name = article.find('h3', {'class': 'name'})  # Récupérer le nom
        price = article.find('div', {'class': 'prc'})  # Récupérer le prix actuel
        old_price = article.find('div', {'class': 'old'})  # Récupérer l'ancien prix

        # Vérifier et extraire le texte si l'élément est trouvé
        columns['name'].append(name.text.strip() if name else 'N/A')
        columns['price'].append(price.text.strip() if price else 'N/A')
        columns['old_price'].append(old_price.text.strip() if old_price else 'N/A')

# Convertir le dictionnaire en DataFrame
data = pd.DataFrame(columns)

# Exporter les données dans un fichier Excel
data.to_excel('Iphone_products.xlsx', index=False)

print("Les données ont été enregistrées dans 'Iphone_products.xlsx'")
