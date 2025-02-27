import streamlit as st
def sub_side():
    with st.sidebar:
        st.divider()
        st.markdown(''':gray[🗂️ Choisissez un projet :]''')
        st.page_link("pages/brevets.py", label="IA de Classification de Brevets", icon="📄")
        st.page_link("pages/Uber_data.py",label="Uber Projet",icon="🚗")
        st.page_link("pages/airport_project.py",label="Airport App",icon="✈️")
        st.page_link("pages/advanced_databases_project.py",label="Luxury Property Management",icon="🏠")
        
        
        