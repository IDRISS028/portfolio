# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:41:37 2024

@author: Dagnogo
"""
import base64
import streamlit as st
import time
import numpy as np
import pandas as pd
from components import side

# Page configuration
st.set_page_config(page_title="A propos de moi", page_icon="🙂",layout="wide")
side.side()


tab1, tab2, tab3, tab4, tab5 = st.tabs(["👋 EMMANUEL DAGNOGO", "🎓Formations", "💼 Expérience Professionnelle", "🧑‍💻 Compétences 🗣️", "🌿 Valeurs & Approche"])
    
with tab1:
    st.subheader("Étudiant Ingénieure(M1) EFREI")
    st.write(
        """
        🚀 **Chaque donnée raconte une histoire. Mon rôle : lui donner une voix.**

        Je suis **Dagnogo Emmanuel**, étudiant ingénieur en **Big Data et Machine Learning** à **l’EFREI Paris**. 
        Passionné par la data, je considère chaque dataset comme une opportunité : résoudre un problème, éclairer une décision, comprendre le monde autrement.

        Cette passion m’a conduit à approfondir mes compétences sur des outils comme **Python, Pandas, TensorFlow, SQL, BERT**, mais aussi à mener des projets concrets.

        **Exemple marquant :**
        Dans le cadre d'un projet académique, **LIPSTIP** nous a sollicités pour développer une IA capable de **prédire le code CPC des brevets** tout en fournissant des explications sur chaque classification.
        Nous avons réalisé l’entièreté du système, de l’IA à l’interface utilisateur, en utilisant notamment :
        - **BERT, TensorFlow** pour le NLP
        - **Python, Pandas, NumPy, BeautifulSoup** pour la manipulation de données
        - **LIME** pour l’interprétabilité
        - **Django** pour l’IHM

        Aujourd’hui, je suis **à la recherche d’un stage ou d’une alternance** dans le domaine de la **Data Science, Data Analysis ou Big Data**. 

        💡 **Curieux, rigoureux et enthousiaste**, je suis prêt à relever vos défis data.
        """
    )
with tab2:
    st.header("🎓 Formation Académique")
    st.subheader("Master en Data et Intelligence Artificielle – EFREI Paris (2023 - 2026)")
    st.write("""
    Formation d’ingénieur spécialisée en **Big Data et Machine Learning**, avec des enseignements axés sur :
    - **Big Data Frameworks (Spark, Hadoop)**  
    - **Cloud Computing (AWS, GCP)**  
    - **Machine Learning & Deep Learning (Python, TensorFlow, Scikit-learn)**  
    - **Datalakes & Intégration de données**  
    - **Programmation Fonctionnelle en Scala**  
    - **Management, Communication & Innovation**
    """)

    st.subheader("Classe Préparatoire Mathématiques - Physique – ESTEM Casablanca MAROC (2021 - 2023)")
    st.write("""
    Formation intensive en **mathématiques avancées** et **physique**, développant :
    - Rigueur scientifique
    - Capacités d’analyse et de raisonnement
    - Aptitude à résoudre des problématiques complexes
    """)
    st.divider()
    st.header("🌐 Autoformation")
    st.write("""
    **🧑‍💻Kaggle – Spécialisations Data Science**
    - **Intro to Machine Learning**
    - **Pandas**  
    - **Data Visualization**  
    - **Feature Engineering**

    **📊Babypips – Forex Trading & Analyse Technique**
    - Formation continue sur les **marchés financiers** et **l’analyse technique**.
    - Développement d’une compréhension des **mouvements du marché** et de l’**interprétation des graphiques**.
    """)
   
    
with tab3:
    st.subheader("🏦 Société Générale – Agent Bancaire (Août 2024)")
    st.write("""
- Gestion des opérations courantes des clients (retraits, dépôts, virements).
- Accueil et orientation de la clientèle vers les services adaptés.
- Développement des compétences en relation client et en gestion des transactions financières.
""")
    st.divider()
    st.subheader("🛒 Phone House – Caissier (Juillet - Août 2020)")
    st.write("""
- Encaissement et gestion des paiements en magasin.
- Accueil et conseil des clients sur les produits et services.
- Mise en place et organisation des rayons.
""")
    st.divider()
    st.subheader("🔍 Points à Valoriser :")
    st.write("""
- **Compétences transférables vers la data :** précision, rigueur, gestion des opérations, relation client.
- **Capacité d’adaptation rapide** à des environnements différents (secteur bancaire et retail).
- **Développement des soft skills :** communication, gestion du stress, esprit d’équipe.
""")
    
    
with tab4:
    st.subheader("🔷 Compétences Techniques")
    st.markdown("""
**Programmation et Développement**  
- Python (Pandas, NumPy, Scikit-learn, TensorFlow, BeautifulSoup, LIME)  
- Scala (Programmation fonctionnelle)  
- SQL (MySQL)  
- Java (Programmation orientée objet)

**🖥️Big Data et Cloud**  
- Spark, Airflow  
- Datalakes, Data Integration  
- Cloud Computing : AWS, GCP

**📊Analyse et Visualisation**  
- Data Analysis : Nettoyage, exploration, préparation de données  
- Machine Learning : Modélisation, évaluation de modèles  
- Deep Learning : Approche NLP avec BERT, réseaux neuronaux  
- Data Visualization : Matplotlib, Power BI

**🌐Développement Web & API**  
- HTML, CSS, JavaScript  
- Frameworks : Django, Svelte, Vue.js  
- REST API

**🛠️Outils & Environnements**  
- GitHub, Jupyter, IntelliJ, VS Code, Pack Office
""")
    st.divider()
    st.subheader("🧠 Soft Skills")
    st.markdown("""
**🎯Compétences Humaines & Transversales**  
- Rigueur et Précision (développées lors des projets data et de la programmation)  
- Curiosité et Veille Technologique (autoformation sur Kaggle, Babypips, suivi des tendances IA)  
- Esprit d’analyse (travail sur Machine Learning, Deep Learning, bases de données)  
- Résolution de Problèmes (projets académiques complexes)  
- Communication et Pédagogie (modules Rhétorique et Argumentation, L’art de rendre compte, Communication éditoriale)  
- Travail en équipe (projets collaboratifs sur l’IA et les bases de données)  
- Gestion du Stress et Adaptabilité (expériences en banque et en caisse)  
- Autonomie (projets personnels et autoformation sur Kaggle)
""")
with tab5:
    st.subheader("🔍 La Donnée comme Levier de Compréhension")
    st.write(
    "Je crois fermement que chaque donnée, aussi infime soit-elle, recèle une véritable histoire. "
    "Mon approche consiste à écouter ces données, à en extraire des informations pertinentes pour éclairer les décisions.\n\n"
    "La donnée n’est pas qu’un amas de chiffres : c’est un moyen de comprendre le passé, d’analyser le présent et d’anticiper l’avenir."
)
    st.divider()
    st.subheader("🤖 IA & Humain : Une Synergie, Pas une Opposition")
    st.write(
    "Je suis convaincu que l’Intelligence Artificielle n’a pas vocation à remplacer l’humain, mais plutôt à l’accompagner dans ses choix.\n\n"
    "Pour moi, une IA performante est une IA explicable, capable d’apporter de la transparence sur ses décisions.\n\n"
    "C’est pourquoi je m’intéresse autant aux outils d’interprétabilité (comme LIME) qu’aux modèles de pointe."
)
    st.divider()
    st.subheader("📈 Rigueur & Impact")
    st.write(
    "Chaque modèle que je conçois est animé par une double exigence :\n\n"
    "- **Fiabilité** : Des algorithmes construits sur des bases solides, avec des résultats interprétables.\n"
    "- **Utilité** : La technologie doit avant tout servir une finalité concrète : améliorer la performance d’une entreprise, optimiser un processus ou offrir une meilleure expérience utilisateur."
)
    st.divider()
    st.subheader("🧠 L’Apprentissage Continu comme Moteur")
    st.write(
    "Le domaine de la Data et de l’IA évolue constamment. C’est pourquoi j’ai fait de la veille technologique et de l’autoformation un réflexe quotidien.\n\n"
    "Je suis convaincu que se remettre en question et explorer de nouvelles approches est essentiel pour rester pertinent dans ce secteur."
)
    st.divider()
    st.subheader("🤝 Collaboration & Partage")
    st.write(
    "Derrière chaque projet réussi, il y a une équipe.\n\n"
    "Je valorise les échanges, l’intelligence collective et je crois que le partage de connaissances est un puissant levier de croissance.\n\n"
    "Construire ensemble, c’est pour moi la clé d’une data qui crée réellement de la valeur."
)