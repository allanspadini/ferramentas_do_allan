import streamlit as st

import os
from dotenv import load_dotenv
import google.generativeai as genai
from senhas import check_password

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

load_dotenv()

genai.configure(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

st.title("Planejamento do Curso")

# Entrada do usuário
endereco = st.text_input("Nome do curso:", "TensorFlow: Aprenda a criar modelos de aprendizado de máquina com Python")

descricao = f"""
            Escreva a descrição de um curso com esse nome:{endereco}. 
            A descrição deve ser em português brasileiro e deve conter apenas um parágrafo dizendo o que a pessoa vai aprender.
            Não escreva nada além da descrição. Descrição:
    """

publico = f"""
            Escreva uma descrição do público alvo de um curso com esse nome:{endereco}. 
            A descrição deve ser em português brasileiro e deve conter Quem vai aprender? 
            Qual o perfil da pessoa que pode se interessar por esse curso? O que a pessoa precisa saber para conseguir acompanhar esse curso?.
            Não escreva nada além da descrição. Descrição:
    """

objetivos = f"""
            Escreva uma descrição dos objetivos de educacionais de um curso com esse nome:{endereco}. 
            Quais competências, habilidades e atitudes você pretende que as pessoas tenham ao final do curso? 
            Para te ajudar a organizar didaticamente esses objetivos, indicamos o uso da Tabela de Objetivos Educacionais ou Taxonomia de Bloom.	
            Não escreva nada além dos objetivos. Os objetivos devem ser expressos em 5 ou 7 bullets points. Cada bullet point deve ser uma competência, habilidade ou atitude, sendo uma única frase com poucas palavras. Objetivos:
    """

# Adiciona um botão para executar a inferência
if st.button("Rodar Inferência"):
    model = genai.GenerativeModel('gemini-2.0-flash')

    response = model.generate_content(descricao)
     
    st.text_area(label="Descrição do curso:", value=response.text, height=200)

    response = model.generate_content(publico)
     
    st.text_area(label="Público alvo e pré-requisitos:", value=response.text, height=200)

    response = model.generate_content(objetivos)
     
    st.markdown(response.text)