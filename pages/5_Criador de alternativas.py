import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.environ.get("GEMINI_API_KEY"),
)


exemplo = '''
ATIVIDADE DE ALTERNATIVA: A função da atenção

Valquíria trabalha em uma empresa de tecnologia que está desenvolvendo um sistema de reconhecimento de áudio para identificar diferentes tipos de sons em gravações, como o latido de um cachorro, o toque de um telefone ou o som de um alarme. Ela percebe que o modelo atual tem dificuldade em distinguir sons similares ou identificar sons com ruídos de fundo. Para melhorar o desempenho do modelo, Val decide adicionar camadas de atenção ao pipeline de processamento.

Qual é o principal benefício esperado ao incluir essas camadas no sistema de reconhecimento de áudio?

A) A camada de atenção ajuda a reduzir a dimensionalidade dos dados, removendo features redundantes.
Justificativa:
Incorreta. A função da camada de atenção não é reduzir a dimensionalidade, ela retorna a entrada com o mesmo tamanho.
B) A camada de atenção melhora a capacidade do modelo de identificar as partes mais relevantes dos espectrogramas, aumentando a precisão na classificação.
Justificativa:
Alternativa Correta!! A camada de atenção melhora o desempenho do modelo ao destacar as partes mais relevantes dos espectrogramas, o que pode levar a uma melhor precisão na tarefa de classificação.
C) A camada de atenção serve para normalizar as entradas, garantindo que todas as features estejam na mesma escala.
Justificativa:
Incorreta. A normalização é realizada pelo norm_layer, não pela camada de atenção.

D) A camada de atenção é responsável por acelerar o treinamento do modelo, reduzindo o número de épocas necessárias.
Justificativa:
Incorreta. Embora a atenção possa contribuir para um aprendizado mais eficiente, seu principal objetivo não é acelerar o treinamento.
'''

conteudo = st.text_area("Conteúdo:", "Roteiro do vídeo")

prompt = f"""
Você é um criador de atividades de alternativa da Alura. 
Eu irei te passar o conteúdo do vídeo no qual você deve se basear para criar uma atividade. 
A atividade deve ser uma questão com 4 alternativas, A, B, C e D. 
A atividade deve começar com um contexto de aplicação, uma situação de mercado onde a pessoa está tentando aplicar o conteúdo de alguma forma.
Três das alternativas devem ser falsas e apenas uma verdadeira. 
Cada alternativa deve ter uma justificativa informando porque ela é verdadeira ou falsa.
A justificativa das alternativas falsas não devem entregar a resposta e a justificativa da alternativa correta devem iniciar com a frase: Alternativa Correta!

Aqui o conteúdo no qual você deve se basear para a construção da atividade:

{conteudo}


Exemplo de uma atividade que segue o padrão descrito:

{exemplo}
"""

# Adiciona um botão para executar a inferência
if st.button("Rodar Inferência"):
    model = genai.GenerativeModel('gemini-1.5-pro')

    response = model.generate_content(prompt)

    #st.markdown(response.text)
    st.text_area(label="Saída:", value=response.text, height=350)