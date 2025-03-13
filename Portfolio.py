# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:26:53 2024

@author: Dagnogo
"""

import streamlit as st
from components import side


st.set_page_config(
    page_title="Portfolio",
    layout="wide"
    #page_icon="",
)

# Sidebar
side.side()


# Image et titre de la page
st.image("static/Ban.jpg",width=1000)  # Remplace avec le chemin de ton image

st.title("✨ Bienvenue sur mon Portfolio")

st.write(
    """
    Bienvenue sur mon espace personnel dédié à la donnée et à l’intelligence artificielle.  
    Ici, je vous invite à découvrir comment les données peuvent devenir des leviers stratégiques  
    et comment l’IA peut enrichir nos décisions.
    """
)
st.divider()
st.subheader("🧑‍💻 Qui suis-je ?")
st.write(
    """
    Je suis **Dagnogo Emmanuel**, étudiant ingénieur en **Big Data et Machine Learning** à **l’EFREI Paris**.  
    Passionné par la donnée et ses multiples applications, je m’efforce de transformer  
    **des chiffres bruts en solutions concrètes et décisions éclairées**.

    **Ma mission :**  
    ➡️ Donner du sens aux données pour agir avec pertinence.
    """
)
st.divider()
st.subheader("📂 Ce que vous trouverez sur ce portfolio :")
st.write(
    """
    - 🔍 **Projets Data & IA** – Des cas concrets en machine learning, NLP, visualisation.  
    - 📊 **Dashboards & Visualisations** – Des outils interactifs pour explorer des données complexes.  
    - 🧠 **Compétences & Parcours** – Un aperçu de mes savoir-faire techniques et humains.  
    - 🌍 **Ma Vision de la Data** – Une approche centrée sur la rigueur, l’explicabilité et l’impact.
    """
)
st.divider()
st.subheader("🚀 Pourquoi la Data & l’IA m’inspirent ?")
st.write(
    """
    Parce que **chaque dataset est une énigme**, chaque modèle est **une boussole**,  
    et chaque visualisation est **une histoire que l’on raconte**.  
    J’aime **débusquer l’invisible dans les données** et **outiller les décideurs**  
    pour qu’ils avancent avec **confiance et clarté**.
    """
)
st.divider()
st.subheader("🤝 Et si nous collaborions ?")
st.write(
    """
    Vous cherchez **un stagiaire ou un alternant motivé** pour donner vie à vos projets data ?  
    Je serais ravi d’échanger avec vous !  

    ➡️ **Contactez-moi ou explorez mes travaux pour en savoir plus.**
    """
)