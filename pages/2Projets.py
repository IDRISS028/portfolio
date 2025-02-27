# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:39:50 2024

@author: Dagnogo
"""
import streamlit as st
from components import side, P_sub_side


# Page configuration
st.set_page_config(page_title="Projets", page_icon="📊", layout="wide")

side.side()
P_sub_side.sub_side()
   
    
    

st.title("🗂️ Mes Projets Data & IA")

st.write(
    """
    Dans cette section, vous trouverez **un aperçu des travaux que j’ai réalisés** dans le domaine de la **Data Science**, du **Machine Learning** et du **Big Data**.  
    Chaque projet est **le reflet de ma passion pour l’analyse, le traitement et la valorisation des données**.

    Mon objectif est **de transformer les données brutes en informations exploitables**, en m’appuyant sur **des modèles d’intelligence artificielle et des outils de visualisation adaptés**.
    """
)
st.divider()
st.subheader("📄 1. Classification de Brevets avec IA Explicable")
st.write(
    """
    **Objectif :** Développer un modèle capable de **prédire le code CPC** d’un brevet à partir de sa description, tout en fournissant **des explications sur ses décisions**.  
    **Technologies :** BERT, TensorFlow, LIME, Pandas, BeautifulSoup, Django  
    **Ce que j’ai appris :**
    - Application concrète du **NLP (Traitement Automatique du Langage)**.
    - Mise en place d’un **modèle explicable** pour garantir la **transparence des prédictions**.
    - Développement d’une **interface utilisateur** pour faciliter l’utilisation du modèle.
    """
)
st.markdown("[👉 Voir le projet](brevets)")
st.divider()

st.subheader("📊 2. Analyse des Trajets Uber - Avril 2014")
st.write(
    """
    **Objectif :** Le projet Uber Analytics vise à **analyser** les tendances des trajets Uber à New York en avril 2014, à l’aide de données issues des enregistrements de trajets..  
    **Technologies :** Python, Streamlit, Pandas, Matplotlib, Seaborn, Plotly 
    
    **Ce que j’ai appris :**
    - Exploration des tendances **temporelles** et **géographiques**.
    - Maîtrise des bibliothèques de **visualisation avancées**.
    - Création d’un **dashboard interactif**.
    """
)
st.markdown("[👉 Voir le projet](Uber_data)")
st.divider()

st.subheader("✈️ 3. Airport App – Analyse des Aéroports et Pistes d’Atterrissage")
st.write(
    """
    **Objectif :** Airport Analytics est une application en Scala qui analyse des fichiers CSV sur les aéroports, pistes d’atterrissage et pays.**.  
    **Technologies :** 
    - Langage : Scala
    - Gestion de projet : sbt
    - Traitement des CSV sans bibliothèque externe
    - Programmation fonctionnelle (case class, objets compagnons, pas de var, for, null…) 
    
    **Ce que j’ai appris :**
    - Manipuler des fichiers CSV manuellement en Scala.
    - Structurer un projet en modules : Parsing, Stockage, Interface utilisateur.
    - Appliquer les principes de la programmation fonctionnelle pour écrire un code clair et robuste.
    """
)
st.markdown("[👉 Voir le projet](airport_project)")
st.divider()

st.subheader("🏠 4. Luxury Property Management – Advanced Databases Project")
st.write(
    """
    **Objectif :**  concevoir et implémenter une **base de données relationnelle** et **NoSQL** pour gérer les **données complexes** du secteur de l’immobilier haut de gamme.  
    **Technologies :** SQL, PL/SQL, Oracle Database, MongoDB, Neo4J, etc.  
    **Ce que j’ai appris :**
- **Conception de bases de données complexes** adaptées aux besoins métiers.
- **Automatisation avec PL/SQL** : gestion des transactions, calcul des commissions, déclenchement d’événements.
- **Modélisation Objet-Relational (ORD)** : création de types personnalisés et héritage.
- **Intégration NoSQL** :
  - **MongoDB** pour la flexibilité documentaire.
  - **Neo4J** pour l’analyse des relations sous forme de graphes.
- **Différences entre SQL et NoSQL** selon les cas d’usage (flexibilité, performances, structuration).
    """
)
st.markdown("[👉 Voir le projet](advanced_databases_project)")
