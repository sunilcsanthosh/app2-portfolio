import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_input("Your Message")
    message = message + "\n" + user_email
    button = st.form_submit_button("Submitt")

    if button:
        send_email(message)