
import streamlit as st
from components import side, P_sub_side

# Configuration de Streamlit
st.set_page_config(
    page_title="brevets",
    layout="wide",
    page_icon="📄"
)

# Titre de la page
st.title("📄 Classification de Brevets avec IA Explicable")

# On affiche le menu de gauche
side.side()

# On affiche le sous-menu de gauche
P_sub_side.sub_side()

tab1, tab2 = st.tabs(["🧑‍💻 Présentation du Projet", "Démo"])
with tab1:
    st.write("""
Ce projet vise à **développer une IA capable de classifier automatiquement les brevets** selon le **code CPC (Cooperative Patent Classification)** en se basant sur la description textuelle de l’invention.  
Une **attention particulière** a été portée à **l’interprétabilité des résultats** afin que l’utilisateur comprenne les raisons derrière chaque prédiction.

Projet réalisé dans le cadre d’un partenariat académique avec **LIPSTIP**.
""")
    st.divider()
    st.subheader("🎯 Objectifs")
    st.write("""
- **Prédire automatiquement le code CPC d’un brevet** à partir de sa description textuelle.
- **Fournir des explications sur les prédictions** grâce à une approche d’**IA explicable**.
- **Développer une interface utilisateur (IHM)** pour faciliter l’utilisation par des non-techniciens.
""")
    st.divider()
    st.subheader("🛠️ Technologies Utilisées")
    st.markdown("""
| Domaine              | Outils et Bibliothèques                                              |
|----------------------|-----------------------------------------------------------------------|
| **NLP et Modèle IA** | BERT, TensorFlow, LIME                                               |
| **Manipulation des Données** | Pandas, NumPy, BeautifulSoup                                      |
| **Développement Web** | Django (Interface Utilisateur)                                       |
| **Entraînement & Évaluation** | Python, Jupyter Notebook                                           |
""", unsafe_allow_html=True)
    st.divider()
    st.subheader("📦 Déroulement du Projet")
    st.write("""
1️⃣ **Préparation des Données**  
- Collecte et nettoyage des descriptions de brevets.  
- Tokenisation et vectorisation avec **BERT**.

2️⃣ **Modélisation**  
- Entraînement d’un **modèle de classification multi-label** pour assigner les codes CPC.  
- Utilisation de **LIME** pour **fournir des explications** sur les prédictions.

3️⃣ **Déploiement d’une Interface**  
- Développement d’un **site web Django** pour permettre aux utilisateurs :
    - **De soumettre une description de brevet**.
    - **De recevoir le code CPC prédit + une explication visuelle**.
""")
    st.divider()
    st.subheader("🏆 Ce que J’ai Appris")
    st.write("""
- **Fine-tuning de BERT** pour une **classification multi-label**.
- **Utilisation de LIME** pour **interpréter les décisions d’un modèle NLP**.
- **Intégration d’une IA dans une application web** avec **Django**.
- **Travail d’équipe sur un projet Data Science & Développement Web**.
""")
    
    
with tab2:
    video_file = open("static/Démo projet classification de brevet.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
    
