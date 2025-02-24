import streamlit as st
import nbformat
from senhas import check_password

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

# Função para dividir o notebook
def split_notebook(notebook_content):
    # Carrega o notebook do conteúdo enviado
    notebook = nbformat.reads(notebook_content, as_version=4)
    
    # Inicializa variáveis
    notebooks = []
    current_notebook = nbformat.v4.new_notebook()
    current_cells = []
    
    for cell in notebook.cells:
        if cell.cell_type == 'markdown' and cell.source.startswith('# Aula'):
            # Se encontrar um novo título de aula
            if current_cells:
                current_notebook.cells = current_cells.copy()
                notebooks.append(current_notebook)
            current_notebook = nbformat.v4.new_notebook()
            current_cells = []
        
        # Adiciona a célula ao notebook corrente
        current_cells.append(cell)
    
    # Adiciona o último notebook
    if current_cells:
        current_notebook.cells = current_cells.copy()
        notebooks.append(current_notebook)
    
    # Cria os notebooks para cada aula acumulando o conteúdo das aulas anteriores
    for i, nb in enumerate(notebooks):
        cumulative_nb = nbformat.v4.new_notebook()
        cumulative_nb.cells = sum([notebooks[j].cells for j in range(i+1)], [])
        
        # Converte o notebook para string
        notebook_str = nbformat.writes(cumulative_nb)
        
        # Salva o notebook correspondente em formato bytes para download
        st.download_button(
            label=f'Baixar aula_{i+1}.ipynb',
            data=notebook_str.encode('utf-8'),
            file_name=f'aula_{i+1}.ipynb',
            mime='application/octet-stream'
        )

# Interface do Streamlit
st.title("Divisor de Notebooks")

uploaded_file = st.file_uploader("Carregue seu arquivo de notebook (.ipynb)", type="ipynb")

if uploaded_file is not None:
    # Lê o conteúdo do arquivo carregado
    notebook_content = uploaded_file.read().decode('utf-8')
    
    # Divide o notebook e cria os links de download
    split_notebook(notebook_content)
