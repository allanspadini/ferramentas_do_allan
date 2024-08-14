import streamlit as st
import nbformat
from groq import Groq
import os
from dotenv import load_dotenv

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Função para extrair o conteúdo de uma aula específica
def extract_lesson_content(notebook_content):
    # Carrega o notebook a partir do conteúdo
    notebook = nbformat.reads(notebook_content, as_version=4)
    
    # Inicializa variáveis
    in_lesson = False
    lesson_content = []
    
    for cell in notebook.cells: 
        # Se estamos na aula, adiciona o conteúdo da célula       
        lesson_content.append(cell.source)
    
    # Concatena todo o conteúdo em uma única string
    lesson_text = "\n".join(lesson_content)
    
    return lesson_text

# Interface do Streamlit
st.title("Em construção")

uploaded_file = st.file_uploader("Carregue seu arquivo de notebook (.ipynb)", type="ipynb")
aula = st.text_input("Aula:")
if uploaded_file is not None:
    # Lê o conteúdo do arquivo carregado
    notebook_content = uploaded_file.read().decode('utf-8')
    
    if st.button("Extrair Conteúdo"):
        # Extrai o conteúdo da aula específica
        content = extract_lesson_content(notebook_content)
        
        prompt = f"""
            Você deve criar 5 bullets sobre indicando conteúdos que o aluno aprendeu na {aula}. 
            Cada bullet deve iniciar com um verbo no infinitivo impessoal. Se houver conteúdo
            antes da aula os bullets devem indicar apenas conteúdo inédito que foi aprendido pelo aluno. 
            Você deve utilizar o conteúdo a seguir para encontrar o conteúdo das aulas: {content}
        """
        # Mostra o conteúdo extraído na interface do Streamlit
        if content:
            chat_completion = client.chat.completions.create(
                            messages=[
                                {
                                    "role": "user",
                                    "content": prompt,
                                }
                            ],
                            model="llama3-70b-8192",
                        )
            resposta = chat_completion.choices[0].message.content
            
            st.text_area("Conteúdo Extraído", resposta, height=300)
