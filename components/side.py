
import streamlit as st

def side():
    with st.sidebar:
        st.page_link("Accueil.py", label="Accueil", icon="🏠")
        st.page_link("pages/1A propos de moi.py", label="À Propos de moi", icon="🤖")
        st.page_link("pages/2Projets.py", label="Projets", icon="📁")
        st.page_link("pages/3CV.py", label="CV", icon="📄")
        st.page_link("pages/4Contact.py", label="Contact", icon="📩")
        