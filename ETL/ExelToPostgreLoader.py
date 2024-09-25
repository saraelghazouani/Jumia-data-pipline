from sqlalchemy import create_engine
import pandas as pd
import os

password = 'your password'
username = 'postgres'
host = "localhost"
database_name = "database name"
port = "5432"
data_directory = r'path\To\the\folder\jumia_ETL'

# Fonction pour extraire les données des fichiers Excel
def extract_data():
    try:
        for file in os.listdir(data_directory):
            # Extraire le nom du fichier sans l'extension
            table_name = os.path.splitext(file)[0]
            # Si le fichier a l'extension ".xlsx"
            if file.endswith(".xlsx"):
                file_path = os.path.join(data_directory, file)
                if os.path.isfile(file_path):
                    # Lire le fichier Excel en DataFrame
                    data_frame = pd.read_excel(file_path)
                    # Charger les données dans la base de données
                    load_data(data_frame, table_name)
    except Exception as error:
        print("Erreur lors de l'extraction des données : " + str(error))

# Fonction pour charger les données dans PostgreSQL
def load_data(data_frame, table_name):
    try:
        rows_imported = 0
        # Créer une connexion à la base de données PostgreSQL
        engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database_name}')
        print(f'Importation de {rows_imported} à {rows_imported + len(data_frame)} lignes...')
        # Charger les données dans une table PostgreSQL
        data_frame.to_sql(table_name, engine, if_exists='replace', index=False)
        rows_imported += len(data_frame)
        print("Données importées avec succès.")
    except Exception as error:
        print("Erreur lors du chargement des données : " + str(error))

# Bloc principal pour exécuter l'extraction et le chargement
if __name__ == '__main__':
    try:
        extract_data()
    except Exception as error:
        print("Erreur lors du processus d'extraction : " + str(error))
