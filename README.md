# ETL Project: Web Scraping, Excel Handling, and PostgreSQL Loading


## Description:

Ce projet ETL (Extract, Transform, Load) vise à extraire des données du site Jumia à l'aide de Beautiful Soup, à les stocker dans un fichier Excel à l'aide de Pandas, puis à transférer ces données dans une base de données PostgreSQL en utilisant SQLAlchemy et Pandas.


## Table des matières

-[Technologies utilisées](#technologies-utilisées)

-[Installation](#installation)

* [Cloner le dépôt](#1-cloner-le-dépôt)

* [Configurer l'environnement Python](#2-configurer-lenvironnement-python)

* [Installer les dépendances](#3-installer-les-dépendances)

* [Configurer la base de données PostgreSQL](#4-configurer-la-base-de-données-postgresql)

-[Exécution du projet](#exécution-du-projet)

-[Structure du projet](#structure-du-projet)

-[Contact](#contact)

## Technologies utilisées

-Python 3.11 : Langage de programmation principal pour le projet.

-Beautiful Soup 4 : Pour le scraping Web.

-Pandas : Pour la manipulation des données et la sauvegarde dans Excel.

-SQLAlchemy : Pour l'intégration avec PostgreSQL.

-PostgreSQL : Base de données relationnelle pour stocker les données des produits.

-Requests : Pour faire des requêtes HTTP aux pages Web.
## Installation 
### 1-Cloner le dépôt
Commencez par cloner le dépôt sur votre machine locale :
```
git clone https://github.com/saraelghazouani/Jumia-data-pipline.git
```
Ensuite, accédez au dossier du projet :
```
cd Jumia-data-pipline
```
### 2-Configurer l'environnement Python
Assurez-vous que Python 3.11 est installé sur votre machine. Vous pouvez vérifier la version de Python avec la commande suivante :
```
python --version
```
### 3-Installer les dépendances
```
pip install beautifulsoup4 pandas sqlalchemy openpyxl psycopg2
```
### 4-Configurer la base de données PostgreSQL
Vous devez avoir une instance de PostgreSQL en cours d'exécution. Si PostgreSQL n'est pas installé, vous pouvez le télécharger et l'installer à partir du [site officiel](https://www.postgresql.org/).

! il est necessaire de changer les parametres (password, username, host, database_name, port, data_directory) dans le fichier ExelToPostgreLoader.py.

## Exécution du projet
1. **Naviguer vers le projet**
   ```
   cd Jumia-data-pipline
   ```
2. **Lancer le script**
   ```
   python scripts/etl_process.py
   ```
3. **Vérification dans PostgreSQL**
   
   Une fois le script exécuté, vous pouvez vous connecter à votre base de données PostgreSQL pour vérifier si les données ont été correctement importées.
    ```
    SELECT * FROM nom_de_la_table;
    ```
## Structure du projet
1-Extraction des données(nom,prix,l'ancien prix) de produits Iphone 15 pro max depuis le site de Jumia[[https://www.jumia.ma/](https://www.jumia.ma/)]].

2-Transformation et organisation des données sous forme tabulaire.

3-Sauvegarde des données dans un fichier Excel.

4-Chargement des données dans une base de données PostgreSQL.
## contact
[Sara elghazouani](https://www.linkedin.com/in/sara-el-ghazouani-378047268/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BzhqlcgsPQZOomNE3aGUlbQ%3D%3D)




