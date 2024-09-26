# ETL Project: Web Scraping, Excel Handling, and PostgreSQL Loading


## Description:

Ce projet ETL (Extract, Transform, Load) vise à extraire des données du site Jumia à l'aide de Beautiful Soup, à les stocker dans un fichier Excel à l'aide de Pandas, puis à transférer ces données dans une base de données PostgreSQL en utilisant SQLAlchemy et Pandas.

## Le flux général est le suivant :

1-Extraction des données de produits depuis le site de Jumia.

2-Transformation et organisation des données sous forme tabulaire.

3-Sauvegarde des données dans un fichier Excel.

4-Chargement des données dans une base de données PostgreSQL.

## Table des matières

-[Technologies utilisées](#technologies-utilisées)

-[Pré-requis](#pré-requis)

-[Installation](#installation)

* Cloner le dépôt

* Configurer l'environnement Python

* Installer les dépendances

* Configurer la base de données PostgreSQL

-Exécution du projet

-Structure du projet

-Données extraites

-[Contact](#contact)

## Technologies utilisées

-Python 3.11 : Langage de programmation principal pour le projet.

-Beautiful Soup 4 : Pour le scraping Web.

-Pandas : Pour la manipulation des données et la sauvegarde dans Excel.

-SQLAlchemy : Pour l'intégration avec PostgreSQL.

-PostgreSQL : Base de données relationnelle pour stocker les données des produits.

-Requests : Pour faire des requêtes HTTP aux pages Web.

## Pré-requis


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
### 3. Installer les dépendances
```
pip install beautifulsoup4 pandas sqlalchemy openpyxl psycopg2
```
### 4. Configurer la base de données PostgreSQL
Vous devez avoir une instance de PostgreSQL en cours d'exécution. Si PostgreSQL n'est pas installé, vous pouvez le télécharger et l'installer à partir du [site officiel](https://www.postgresql.org/).
## contact
[Sara elghazouani](https://www.linkedin.com/in/sara-el-ghazouani-378047268/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BzhqlcgsPQZOomNE3aGUlbQ%3D%3D)







![2018_3large_Jumia](https://github.com/user-attachments/assets/6422d54e-ae5c-4a37-8d3b-eb57ac69135c)


![Postgre-data](https://github.com/user-attachments/assets/4fce3a85-7b12-402f-92e3-f125e41eaf29)


```
git init

```

