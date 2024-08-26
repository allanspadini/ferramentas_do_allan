import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a API do Google Generative AI
genai.configure(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

# Carregar o arquivo de imagem usando o file_uploader do Streamlit
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Salvar o arquivo carregado temporariamente
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Fazer o upload da imagem para o Google Generative AI
    sample_file = genai.upload_file(path="temp_image.jpg")
    

    # Criar um modelo de visão
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Gerar o alt-text para a imagem
    prompt = "Crie um alt-text descritivo e conciso para esta imagem."
    response = model.generate_content([prompt, sample_file])

    # Exibir o alt-text gerado
    st.subheader("Alt-text gerado:")

    #Gerar o prompt para o modelo de visão

    prompt = "Crie um prompt para o modelo de visão para gerar uma imagem que corresponda ao alt-text gerado."
    response = model.generate_content([prompt, sample_file])

    st.text_area(label="Saída:", value=response.text, height=350)



    
        

