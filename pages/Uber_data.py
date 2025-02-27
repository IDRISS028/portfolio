import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk
import time
import numpy as np
import plotly.express as px
from components import side,P_sub_side



st.set_page_config(
    page_title="Uber Projet",
    layout="wide",
    page_icon="🚗"
)

# Titre de la page
st.title("🚗 Analyse des Trajets Uber - Avril 2014")

# On affiche le menu de gauche
side.side()

# On affiche le sous-menu de gauche
P_sub_side.sub_side()

    # Charger le dataset
@st.cache_data
def load_data():
    df = pd.read_csv('Datasets/uber-raw-data-apr14.csv')

    # Convertir la colonne 'Date/Time' en datetime
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    df['DayOfWeek'] = df['Date/Time'].dt.weekday
    df['Hour'] = df['Date/Time'].dt.hour
    return df
df = load_data()

# Fonction pour compter le nombre de lignes 
def count_rows(rows):
    return len(rows)

    
# Ajouter un aperçu du dataset
st.subheader("Aperçu du Dataset")
st.write(df.iloc[0:5,0:4])  # Afficher les 5 premières lignes du dataset
    
# Description du dataset
st.subheader("Description du Dataset")
st.write("""
Le dataset représente les trajets Uber effectués au mois d'avril 2014 à New York City. Il contient 564 516 enregistrements, avec les informations suivantes :
- **Date/Time** : La date et l'heure de départ du trajet.
- **Lat** : La latitude du point de départ du trajet.
- **Lon** : La longitude du point de départ du trajet.
- **Base** : Le code de base (station ou région associée) qui a généré le trajet.

Le but de cette analyse est d'explorer les tendances temporelles et géographiques des trajets Uber, afin d'identifier des périodes de forte demande et les zones les plus actives à New York.
""")

    # Option pour sélectionner une visualisation
option = st.selectbox(
    'Sélectionnez une visualisation :',
    ('Trajets par jour de la semaine', 'Trajets par heure', 'Carte Heatmap des trajets', 'Trajets par Base', 'Heatmap par heure et jour de la semaine','Heatmap dynamique')
    )

    # Visualisation 1 : Trajets par jour de la semaine
if option == 'Trajets par jour de la semaine':
    st.subheader("Nombre de trajets par jour de la semaine")
    plt.figure(figsize=(10, 6))
    sns.countplot(x='DayOfWeek', data=df)
    plt.title('Nombre de trajets par jour de la semaine')
    plt.xticks(np.arange(7), 'Lun Mar Mer Jeu Ven Sam Dim'.split())
    st.pyplot(plt)
        
        #Insights et Interpretations
    st.subheader("Insights:")
    st.write("""
                - **Mercredi** est le jour qui enregistre le plus grand nombre de trajets, avec plus de 100 000 trajets.
                - **Dimanche** enregistre le nombre de trajets le plus faible, avec un peu moins de 60 000 trajets.
                - Il y a une tendance générale montrant que le milieu de la semaine (mardi, mercredi, jeudi) est plus actif en termes de trajets Uber que le début et la fin de la semaine (lundi, samedi, dimanche).
                - **Vendredi**  est également un jour actif, proche des volumes du mercredi.""")
        
    st.subheader("Interpretations:")
    st.write("""
                - On pourrait supposer que la demande d'Uber augmente pendant la semaine de travail, notamment pour des trajets professionnels ou des déplacements réguliers, et diminue le week-end, lorsque moins de personnes ont besoin de se déplacer pour des raisons professionnelles.
                - **Mercredi** étant le jour le plus actif pourrait être lié à une combinaison d'activités professionnelles et sociales en milieu de semaine, tandis que la baisse observée le dimanche pourrait être attribuée à la nature plus calme du week-end.
                """)
        
    st.write("""Cet insight peut être utile pour planifier des stratégies commerciales, comme augmenter la disponibilité des voitures les jours les plus chargés ou prévoir des campagnes marketing pendant les périodes plus calmes.""")


# Visualisation 2 : Trajets par heure de la journée
elif option == 'Trajets par heure':
    st.subheader("Nombre de trajets par heure de la journée")
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Hour', data=df)
    plt.title('Nombre de trajets par heure de la journée')
    st.pyplot(plt)
        
        #Insights et Interpretations
    st.subheader("Insights:")
    st.write("""
                - **Deux pics d’activité principaux :** Le premier pic se situe entre 6h et 8h du matin, avec environ 20 000 à 30 000 trajets. Ce pic correspond probablement à l'heure de pointe matinale lorsque les gens se déplacent pour aller au travail.Le second et plus grand pic se situe entre 15h et 19h, atteignant un maximum de plus de 40 000 trajets à 17h. Cela reflète probablement l’heure de pointe en fin de journée, au moment où les gens rentrent chez eux après le travail.   
                - **Faible activité durant la nuit :** Entre minuit et 5h du matin, le nombre de trajets est très bas, souvent en dessous de 10 000. Cela suggère une faible demande de déplacements pendant les heures tardives.
                - **Augmentation progressive en début de journée :** À partir de 5h du matin, on observe une augmentation progressive des trajets, indiquant que l’activité commence tôt et se renforce jusqu’à l’heure de pointe matinale.
                - **Relâchement après 18h :** Après le pic de 17h, le nombre de trajets diminue lentement mais reste relativement élevé jusqu’à 21h, avant de chuter davantage en fin de soirée.""")
        
    st.subheader("Interpretations:")
    st.write("""
                Ce graphique confirme que les courses Uber sont surtout utilisées aux heures de pointe en semaine, pour les trajets liés au travail, et augmentent également en fin de semaine, probablement en lien avec les activités de loisirs. Le mercredi et le vendredi semblent être les jours où la demande est la plus forte.
                """)
        
        
    # Visualisation 3 : Carte Heatmap des trajets
elif option == 'Carte Heatmap des trajets':
    st.subheader("Carte Heatmap des trajets Uber à New York")

        
    # Configurer les données pour Pydeck
    view_state = pdk.ViewState(
            latitude=40.7128,
            longitude=-74.0060,
            zoom=11,
            pitch=50,
        )

    # Créer une couche de carte de chaleur
    layer = pdk.Layer(
            "HeatmapLayer",
            data=df[['Lat', 'Lon']],
            get_position=['Lon', 'Lat'],
            radius=100,
            elevation_scale=50,
            elevation_range=[0, 300],
            pickable=True,
            extruded=True,
        )
        
           
    # Rendu de la carte
    map_deck = pdk.Deck(layers=[layer], initial_view_state=view_state)
    st.pydeck_chart(map_deck)
       
        
        

        
elif option == 'Trajets par Base':
    st.subheader("Nombre de trajets par Base")
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Base', data=df, order=df['Base'].value_counts().index)
    plt.title('Nombre de trajets par Base')
    plt.xticks(rotation=45)
    st.pyplot(plt)
        
elif option == 'Heatmap par heure et jour de la semaine':
    st.subheader("Modèle hebdomadaire des trajets")
    df2 = df.groupby(['DayOfWeek', 'Hour']).apply(count_rows).unstack()
    st.write(df2.head(7))
    heatmap = sns.heatmap(df2,linewidths =.5)
    plt.title('Heatmap par heure et jour de la semaine - Uber - April 2014',fontsize=15)
    heatmap.set_yticklabels(('Lun Mar Mer Jeu Ven Sam Dim').split(), rotation='horizontal')
    st.pyplot(plt)

        #Insights et Interpretations
    st.subheader("Insights:")
    st.write("""
                - **Activité concentrée en semaine le matin et l'après-midi :** Le volume est élevé entre 6h et 8h, puis entre 15h et 21h, du mardi au jeudi, ce qui suggère que les utilisateurs utilisent Uber principalement pour leurs trajets domicile-travail. Le mercredi présente un pic particulièrement important dans ces plages horaires.
                - **Vendredi après-midi :**  Le vendredi a une activité notable dans l'après-midi, de 15h à 22h, qui est plus élevée que celle observée en début de matinée.
                - **Week-ends plus calmes :** Le samedi et le dimanche montrent une activité plus dispersée et globalement moins intense, avec des pics modérés en début de soirée.
                - **Forte diminution durant la nuit :** Les courses sont très rares pendant la nuit, surtout entre minuit et 5h du matin, indiquant une faible demande pour les trajets nocturnes.""")
        
    st.subheader("Interpretations:")
    st.write("""
                Ce graphique confirme que les courses Uber sont surtout utilisées aux heures de pointe en semaine, pour les trajets liés au travail, et augmentent également en fin de semaine, probablement en lien avec les activités de loisirs. Le mercredi et le vendredi semblent être les jours où la demande est la plus forte.
                """)
        
        
elif option == "Heatmap dynamique":
    st.subheader("Heatmap dynamique des trajets")
    # Extraire les jours de la semaine et les heures
    df['WeekDay'] = df['Date/Time'].dt.day_name()  # Noms des jours
    df['Hour'] = df['Date/Time'].dt.hour  # Heures de la journée

        # Compter le nombre de trajets par jour et par heure
    df2 = df.groupby(['WeekDay', 'Hour']).size().reset_index(name='Counts')

        # Réorganiser les jours de la semaine
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df2['WeekDay'] = pd.Categorical(df2['WeekDay'], categories=days_order, ordered=True)

    # Créer une heatmap interactive avec Plotly
    fig = px.density_heatmap(
        df2, 
        x='Hour', 
        y='WeekDay', 
        z='Counts', 
        color_continuous_scale='Viridis', 
        labels={'DayOfWeek': 'Jour de la semaine', 'Hour': 'Heure de la journée', 'Counts': 'Nombre de trajets'},
        title='Heatmap interactive par heure et jours de la semaine - Uber - Avril 2014'
        )

        # Afficher le graphique dans Streamlit
    st.plotly_chart(fig)
        
    
