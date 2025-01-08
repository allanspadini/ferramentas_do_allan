import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.environ.get("GEMINI_API_KEY"),
)


exemplo = '''

Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.


'''


tema = st.text_area("Tema:", "Tema/Descrição do exercício")

prompt = f"""
Você é um criador de exercícios da Alura. Eu irei te passar o tema sobre qual você deve se basear para criar o exercício. Os exercícios são sempre relacionados à Ciência de Dados e deve ser construído um contexto de aplicação relacionado a essa área.
Não precisa apresentar solução para o exercício nessa etapa. 
Este é o tema do exercício:
{tema}


Exemplo de exercício para você ter como base:

{exemplo}
"""

# Adiciona um botão para executar a inferência
if st.button("Rodar Inferência"):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    response = model.generate_content(prompt)

    #st.markdown(response.text)
    st.text_area(label="Exercício:", value=response.text, height=350)

    prompt2 = f"""
        Preciso que apresente o código que resolve o problema e logo em seguida a explicação da resposta. Problema: {response.text}.

        Leve em consideração que esse é um exercício sobre o tema {tema}

    """
    response = model.generate_content(prompt2)
    st.text_area(label="Solução:", value=response.text, height=350)