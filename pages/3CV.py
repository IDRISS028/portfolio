

import streamlit as st
from components import side

# Page configuration
st.set_page_config(page_title="CV", page_icon="📄", layout="wide")

# Sidebar
side.side()


st.write(
    """
    Actuellement **à la recherche d’une alternance ou d’un stage** dans le domaine de la **Data Science, Big Data ou Machine Learning**, je souhaite **mettre mes compétences au service d’une entreprise innovante**, pour **transformer la donnée en véritable levier de performance**.
    """
)


# Load the PDF file and set the download button
pdf_path = "static/CV_EMMANUEL_DAGNOGO.pdf"

# Read and display the PDF using an iframe
with open(pdf_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    st.download_button(label="Télécharger mon CV", data=PDFbyte, file_name="CV_EMMANUEL_DAGNOGO.pdf", mime='application/octet-stream')

st.image("static/CV.png", caption="My Curiculum Vitæ")


