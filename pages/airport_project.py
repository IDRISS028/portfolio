import streamlit as st
from components import side, P_sub_side

# Configuration de Streamlit
st.set_page_config(
    page_title="Airport App",
    layout="wide",
    page_icon="✈️"
)

# Titre de la page
st.title("✈️ Airport App – Analyse des Aéroports et Pistes")

# On affiche le menu de gauche
side.side()

# On affiche le sous-menu de gauche
P_sub_side.sub_side()

tab1, tab2 = st.tabs(["🧑‍💻 Présentation du Projet", "Démo"])

with tab1:
    st.write("""
Ce projet est une application en **Scala** permettant d’explorer les données relatives aux **aéroports, pays et pistes d’atterrissage** à partir de fichiers CSV.  
L’application offre des fonctionnalités de **recherche** et de **rapports analytiques** sur les infrastructures aéroportuaires à travers le monde.
""")

    st.subheader("🛠️ Fonctionnalités Clés")
    st.markdown("""
- 🔍 **Recherche d'Aéroports par Pays** (nom ou code) avec recherche partielle (fuzzy search).
- 📊 **Génération de Rapports** :
  - Top 10 des pays avec le plus d’aéroports / moins d’aéroports.
  - Types de pistes par pays.
  - Top 10 des identifiants de pistes les plus fréquents.
""")
    st.divider()
    st.subheader("🚀 Parties Avancées Implémentées")
    st.write("""
✅ Recherche Fuzzy sur les noms de pays.  
✅ Traitement multi-fichiers CSV sans bibliothèques.  
✅ Séparation Parsing / Stockage / Interface Utilisateur.  
✅ Usage de la programmation fonctionnelle Scala (sans var, sans boucle for).
""")
    st.divider()
    st.subheader("🧑‍💻 Technologies Utilisées")
    st.write("""
- Langage : **Scala**  
- Gestion de projet : **sbt**  
- Manipulation de CSV : **Sans bibliothèque externe**  
- Paradigme : **Programmation fonctionnelle**
""")
    st.divider()
    st.subheader("🏆 Compétences Développées")
    st.write("""
- Programmation fonctionnelle avancée en Scala.
- Parsing manuel de fichiers CSV.
- Conception modulaire et architecture propre.
- Implémentation de recherche partielle.
- Génération d’analyses et de rapports sur des données réelles.
""")
    
with tab2:
    video_file = open("static/airport project demo.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)