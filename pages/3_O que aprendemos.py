import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from senhas import check_password

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

load_dotenv()

genai.configure(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

exemplo = '''
Nessa aula, você aprendeu a:
Utilizar alguns hiperparâmetros do XGBoost;
Experimentar a técnica de busca aleatória pelos melhores hiperparâmetros;
Experimentar a técnica de busca em grade pelos melhores hiperparâmetros;
Selecionar os melhores hiperparâmetros;
Analisar as métricas do modelo ajustado;
Comparar os resultados dos modelos antes e após o ajuste.

'''

conteudo = st.text_area("Conteúdo:", "Roteiro da aula")


prompt = f"""
Você é um criador de atividade O que aprendemos da Alura. Eu irei te passar o conteúdo da aula no qual você deve se basear para criar uma atividade o que aprendemos. 
Nessa atividade devemos ter de 3 a 5 bullets falando um tópico que aprendemos na aula. Cada bullet deve sempre iniciar com um verbo e ser finalizado com ponto e vírgula. Além disso, cada bullet deve ser apenas uma frase simples e curta.

Conteúdo da aula:

{conteudo}


Exemplo de como o conteúdo deve ser organizado na atividade:

{exemplo}
"""

# Adiciona um botão para executar a inferência
if st.button("Rodar Inferência"):
    model = genai.GenerativeModel('gemini-2.0-flash')

    response = model.generate_content(prompt)

    #st.markdown(response.text)
    st.text_area(label="Saída:", value=response.text, height=350)