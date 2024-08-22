import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

exemplo = '''
Nessa aula, você aprendeu como:

Instalar a biblioteca de escaneamento de códigos de barras do ML Kit no Android Studio, utilizando uma abordagem desacoplada;
Configurar o BarcodeScannerOptions para habilitar a detecção de todos os tipos de códigos de barras;
Preparar a imagem de entrada para o scanner utilizando através do InputImage.fromMediaImage;
Implementar o processamento da imagem e a detecção de códigos, incluindo como fechar o proxy e adicionar logs para verificar os resultados.

'''

conteudo = st.text_area("Conteúdo:", "Roteiro da aula")


prompt = f"""
Você é um criador de atividade O que aprendemos da Alura. Eu irei te passar o conteúdo da aula no qual você deve se basear para criar uma atividade o que aprendemos. 
Nessa atividade devemos ter de 3 a 5 bullets falando um tópico que aprendemos na aula. Cada bullet deve sempre iniciar com um verbo.

Conteúdo da aula:

{conteudo}


Exemplo de como o conteúdo deve ser organizado na atividade:

{exemplo}
"""

# Adiciona um botão para executar a inferência
if st.button("Rodar Inferência"):
    model = genai.GenerativeModel('gemini-1.5-flash-latest')

    response = model.generate_content(prompt)

    #st.markdown(response.text)
    st.text_area(label="Saída:", value=response.text, height=350)