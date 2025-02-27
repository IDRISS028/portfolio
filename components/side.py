
import streamlit as st

def side():
    with st.sidebar:
        st.html("""
    <!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio Data - Sidebar</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            background-color: #1C1C1E;
            color: white;
        }
        .sidebar {
            background-color: #1C1C1E;
            padding-top: 20px;
        }
        .sidebar .header {
            display: flex;
            align-items: center;
            padding: 10px 20px;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-bottom: 2px solid #ffffff33;
        }

        .sidebar a {
            display: block;
            padding: 15px 20px;
            color: white;
            text-decoration: none;
            transition: background 0.3s ease, color 0.3s ease;
            border-left: 4px solid transparent;
        }
        .sidebar a:hover {
            background-color: #1A73E8;
            color: #ffffff;
            border-left-color: #00D4FF;
        }
        
        .contact-btn {
    display: block;
    text-align: center;
    background-color: #ff4b4b;
    color: white;
    padding: 10px;
    border-radius: 8px;
    font-weight: bold;
    text-decoration: none;
    margin-top: 20px;
    transition: background-color 0.3s;
}

.contact-btn:hover {
    background-color: #ff3333;
}
        
    </style>
</head>
<body>
    <div class="sidebar">
        <div class="header">
            🎓Emmanuel DAGNOGO
        </div>
        <a href="/" class="active">🏠 Accueil</a>
        <a href="A_propos_de_moi"> 🤖 À Propos de moi</a>
        <a href="Projets">📊 Projets</a>
        <a href="CV">📄 CV</a>
        <a href="Contact" class="contact-btn">📧 Contact</a> 
    </div>
</body>
</html>
    """)