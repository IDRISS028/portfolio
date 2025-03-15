# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:26:53 2024

@author: Dagnogo
"""

import streamlit as st
from components import side
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Accueil",
    layout="wide"
    #page_icon="",
)

# Sidebar
side.side()


# Image et titre de la page
#st.image("static/Ban.jpg",width=1000)  # Remplace avec le chemin de ton image
################################################################
# From sahirmaharaj
particles_js = """<!DOCTYPE html> 
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Particles.js</title>
  <style>
  #particles-js {
    position: fixed;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    z-index: -1; /* Send the animation to the back */
  }
  .content {
    position: relative;
    z-index: 1;
    color: white;
  }
  
</style>
</head>
<body>
  <div id="particles-js"></div>
  <div class="content">
    <!-- Placeholder for Streamlit content -->
  </div>
  <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  <script>
    particlesJS("particles-js", {
      "particles": {
        "number": {
          "value": 500,
          "density": {
            "enable": true,
            "value_area": 800
          }
        },
        "color": {
          "value": "#ffffff"
        },
        "shape": {
          "type": "circle",
          "stroke": {
            "width": 0,
            "color": "#000000"
          },
          "polygon": {
            "nb_sides": 5
          },
          "image": {
            "src": "img/github.svg",
            "width": 100,
            "height": 100
          }
        },
        "opacity": {
          "value": 0.5,
          "random": false,
          "anim": {
            "enable": false,
            "speed": 1,
            "opacity_min": 0.2,
            "sync": false
          }
        },
        "size": {
          "value": 2,
          "random": true,
          "anim": {
            "enable": false,
            "speed": 40,
            "size_min": 0.1,
            "sync": false
          }
        },
        "line_linked": {
          "enable": true,
          "distance": 100,
          "color": "#ffffff",
          "opacity": 0.22,
          "width": 1
        },
        "move": {
          "enable": true,
          "speed": 0.5,
          "direction": "none",
          "random": false,
          "straight": false,
          "out_mode": "out",
          "bounce": true,
          "attract": {
            "enable": false,
            "rotateX": 600,
            "rotateY": 1200
          }
        }
      },
      "interactivity": {
        "detect_on": "canvas",
        "events": {
          "onhover": {
            "enable": true,
            "mode": "grab"
          },
          "onclick": {
            "enable": true,
            "mode": "repulse"
          },
          "resize": true
        },
        "modes": {
          "grab": {
            "distance": 100,
            "line_linked": {
              "opacity": 1
            }
          },
          "bubble": {
            "distance": 400,
            "size": 2,
            "duration": 2,
            "opacity": 0.5,
            "speed": 1
          },
          "repulse": {
            "distance": 200,
            "duration": 0.4
          },
          "push": {
            "particles_nb": 2
          },
          "remove": {
            "particles_nb": 3
          }
        }
      },
      "retina_detect": true
    });
  </script>
</body>
</html>
"""
components.html(particles_js, height=370, scrolling=False)
################################################################
st.title("Bienvenue sur mon Portfolio")

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