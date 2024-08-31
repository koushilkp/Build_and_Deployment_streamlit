import google.generativeai as genai
import streamlit as st
import os
import PIL.Image

#function to get the Gemini Ai response
def get_gemini_response(api_key_Gemini,prompt,image):
    genai.configure(api_key=api_key_Gemini)  
    model=genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt,image])
    return response.text

#initalize the stremalit page
st.set_page_config(page_title="Gemini vision bot Demo AI")

st.header("Gemini vision bot Demo AI")

#input field for the Google API Key
# api_key_Gemini = st.text_input("Enter your Google API Key",type="password")
api_key_Gemini = st.secrets["api_key_Gemini"]


# file uploader to allow the user to upload an image
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None

# Button to sumit the request Submit")
sumbit = st.button("Tell me about the image")

# Input promt from the user
prompt = st.text_input("Input Prompt (eg: Describe the image in detail): ",key="input")

# Display the uploaded image
if uploaded_image is not None:
    image = PIL.Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


# if the the sumbit button is clicked,congigure the gemini api and get the response
if sumbit and api_key_Gemini and image is not None:
    try:
        response = get_gemini_response(api_key_Gemini,prompt,image)
        st.subheader("Gemini Response:")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

