import streamlit as st
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import google.generativeai as genai
from senhas import check_password

if not check_password():
    st.stop()  # Do not continue if check_password is not True.


# Entrada do usuário
endereco = st.text_input("Link:", "https://pt.wikipedia.org/wiki/Ci%C3%AAncia_de_dados")
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

genai.configure(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

# Adiciona um botão para executar a inferência
if st.button("Rodar Inferência"):

    # Fazendo a requisição HTTP para obter o conteúdo da página
    response = requests.get(endereco)
    # Parsing do conteúdo HTML com BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extraindo todo o texto da página
    text = soup.get_text()
    # Removendo espaços em branco excessivos
    text = ' '.join(text.split())
    # Criando o índice e executando a query
    prompt = f"""
            Escreva o enderecão da página no formato [Título da página](endereço da página). 
            Aqui o endereço:{endereco}. 
            Na linha de baixo escreva um texto de um parágrado em português brasileiro explicando porque o
            conteúdo a seguir é bom para quem está estudando o tema. Inicie
            o texto com o símbolo > seguido de espaço e não utilize 
            palavras como o texto é bom porque, apenas explique porque ele é útil. Conteúdo:{text}
    """
    
    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    response = model.generate_content(prompt)
    st.text_area(label="Output Data:", value=response.text, height=350)
