import streamlit as st
import requests
import re

WEBHOOK_URL = st.secrets["webhook_url"]

def is_vaild_email(email_input):
    # basic of Regex to find the correct Email address
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email_input) is not None


def contact_form():
    with st.form('Contact form'):
        name = st.text_input('Enter your name')
        email_input = st.text_input('Enter your email')
        message_input = st.text_area('Enter your message')
        submitted = st.form_submit_button('Submit')

        if submitted:
            if not WEBHOOK_URL:
                st.error('The Email Address is not Set up',icon="📧")
                st.stop()
            if not name:
                st.error('Please enter your name',icon="🧑‍💻")
                st.stop()
            if not email_input:
                st.error('Please enter your email',icon="📧")
                st.stop()
            if not is_vaild_email(email_input):
                st.error('Please enter a valid email',icon="📧")
                st.stop()
            if not message_input:
                st.error('Please enter your message',icon="💬")
                st.stop()

            st.success('Your message has been sent',icon="📨")

            #prepare the Dictionary file 
            data = {
                "name": name,
                "email_input": email_input,
                "message_input": message_input
                }
            
            response =requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200 :
                st.success('Your message has been seen',icon="🤝")
            else:
                st.error('Please enter the Correct data',icon="❌")
                

            # WEBHOOK tools Name "pabbly" or "zappya" or "slack"

