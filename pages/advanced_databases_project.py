import streamlit as st
from components import side, P_sub_side

# Configuration de Streamlit
st.set_page_config(
    page_title="Luxury Property Management",
    layout="wide",
    page_icon="🏠"
)

# Titre de la page
st.title("🏠 Luxury Property Management – Advanced Databases Project")

# On affiche le menu de gauche
side.side()

# On affiche le sous-menu de gauche
P_sub_side.sub_side()



st.write("""
Ce projet est une **application de gestion de propriétés de luxe** développée dans le cadre du module **Advanced Databases**.  
L’objectif était de **concevoir et implémenter une base de données relationnelle et NoSQL** pour gérer les données complexes du secteur de l’immobilier haut de gamme.
""")
st.divider()
st.subheader("🎯 Objectifs du Projet")
st.write("""
- **Concevoir une base relationnelle normalisée** pour représenter les propriétés, transactions et clients.
- **Automatiser la gestion des commissions et des transactions** via **PL/SQL (triggers, procédures)**.
- **Utiliser des approches Object-Relational (ORD)** pour modéliser des entités complexes comme les annexes (piscines, garages, maisons d’hôtes).
- **Intégrer NoSQL :**
  - **MongoDB** pour les descriptions multimédia et avis clients.
  - **Neo4J** pour les relations entre clients et propriétés.
- **Comparer SQL vs NoSQL** pour évaluer les avantages selon le type de données.
""")
st.divider()
st.subheader("🛠️ Technologies Utilisées")
st.markdown("""
| Aspect                  | Outils et Langages                                  |
|--------------------------|----------------------------------------------------|
| **Base Relationnelle**    | SQL, PL/SQL, Oracle Database                      |
| **Programmation**         | PL/SQL (procédures, triggers, packages)           |
| **Object-Relational**     | Types, héritage, tables imbriquées                 |
| **NoSQL – Document**      | MongoDB                                           |
| **NoSQL – Graphes**       | Neo4J                                             |
| **Modélisation**          | E/R, modèle logique, normalisation (1NF à 6NF)   |
""", unsafe_allow_html=True)
st.divider()
st.subheader("🏆 Ce que J’ai Appris")
st.write("""
- **Conception de bases de données complexes** adaptées aux besoins métiers.
- **Automatisation avec PL/SQL** : gestion des transactions, calcul des commissions, déclenchement d’événements.
- **Modélisation Objet-Relational (ORD)** : création de types personnalisés et héritage.
- **Intégration NoSQL** :
  - **MongoDB** pour la flexibilité documentaire.
  - **Neo4J** pour l’analyse des relations sous forme de graphes.
- **Différences entre SQL et NoSQL** selon les cas d’usage (flexibilité, performances, structuration).
""")
st.divider()
st.subheader("📦 Fonctionnalités Clés")
st.write("""
- Gestion des **propriétés** (adresse, type, surface, équipements…).
- Suivi des **transactions** (ventes, locations, commissions dynamiques).
- Gestion des **visites VIP** et interactions clients.
- **Automatisation des calculs fiscaux et commissions** via PL/SQL.
- **Exploration des relations clients-propriétés** avec Neo4J.
""")
