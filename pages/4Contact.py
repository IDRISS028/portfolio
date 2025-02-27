import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from components import side


# Page configuration
st.set_page_config(page_title="Contact", page_icon="📩", layout="wide")

# Appel du composant de la sidebar
side.side()

st.title("📩 Contactez-moi")

st.write(
    """
    Vous avez un projet data à concrétiser ou vous recherchez un collaborateur passionné par l’exploitation des données et l’intelligence artificielle ?  
    Je suis à votre disposition pour échanger sur vos besoins et sur **comment mes compétences peuvent contribuer à vos projets**.
    """
)

st.subheader("🧑‍💻 Coordonnées")
st.write(
    """
    - 📧 **Email :** idrissss.dagnogo@gmail.com  
    - 📞 **Téléphone :** +33 7 44 20 43 01  
    - 🔗 **LinkedIn :** [Mon profil LinkedIn](https://www.linkedin.com/in/emmanuel-idriss-dagnogo-747459292/)  
    """
)

st.subheader("📬 Laissez-moi un message :")
with st.form(key='contact_form'):
    nom = st.text_input("Votre nom")
    email_utilisateur = st.text_input("Votre email")
    message_utilisateur = st.text_area("Votre message")

    submit_button = st.form_submit_button("Envoyer")

if submit_button:
    if nom and email_utilisateur and message_utilisateur:
        try:
            # Configuration de l'envoi
            expéditeur = st.secrets.contact.expéditeur
            mot_de_passe = st.secrets.contact.mot_de_passe
            destinataire = st.secrets.contact.destinataire

            # Création du message
            message = MIMEMultipart()
            message["From"] = expéditeur
            message["To"] = destinataire
            message["Subject"] = f"Nouveau message de {nom} via Portfolio"

            # Corps de l'email
            corps_message = f"""
            Vous avez reçu un message via votre portfolio :

            Nom : {nom}
            Email : {email_utilisateur}
            
            Message :
            {message_utilisateur}
            """
            message.attach(MIMEText(corps_message, "plain"))

            # Connexion au serveur SMTP
            serveur_smtp = smtplib.SMTP("smtp.gmail.com", 587)
            serveur_smtp.starttls()
            serveur_smtp.login(expéditeur, mot_de_passe)

            # Envoi du message
            serveur_smtp.sendmail(expéditeur, destinataire, message.as_string())
            serveur_smtp.quit()

            st.success(f"Merci {nom} ! Votre message a bien été envoyé. Je vous contacterai à l'adresse {email_utilisateur} très prochainement.")

        except Exception as e:
            st.error(f"Une erreur est survenue lors de l'envoi du message : {e}")

    else:
        st.error("Veuillez remplir tous les champs.")
