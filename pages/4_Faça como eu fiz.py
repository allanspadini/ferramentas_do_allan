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
FAÇA COMO EU FIZ: Treinando a sua própria rede

Conteúdo

Nesta aula, aprendemos como treinar uma rede neural para classificação de áudio usando o TensorFlow e Keras.

Agora é sua vez de praticar, fazendo o mesmo no seu projeto!

**Objetivo:** Treinar uma rede neural para classificar áudios em diferentes categorias e analisar os resultados do treinamento.

**Passo a passo:**

1. **Criar o modelo da rede neural:**
2. **Compilar o modelo:**
3. **Treinar o modelo:**
4. **Analisar os resultados do treinamento:**

Opinião da pessoa instrutora

**Exemplo de código:**

```python
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Criar o modelo
model_time_domain = models.Sequential([
    layers.Input(shape=(16000, 1)),
    layers.Conv1D(16, kernel_size=3, activation='relu'),
    layers.MaxPooling1D(pool_size=2),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(36, activation='softmax')
])

# Compilar o modelo
model_time_domain.compile(optimizer='adam',
                          loss='sparse_categorical_crossentropy',
                          metrics=['accuracy'])

# Treinar o modelo
history_time_domain = model_time_domain.fit(train_dataset, epochs=10, validation_data=val_dataset)

# Plotar o histórico
def plot_history(history):
    # Resumo do histórico de precisão
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Acurácia de Treinamento')
    plt.plot(history.history['val_accuracy'], label='Acurácia de Validação')
    plt.title('Acurácia do Modelo')
    plt.xlabel('Época')
    plt.ylabel('Acurácia')
    plt.legend(loc='lower right')

    # Resumo do histórico de perda
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Perda de Treinamento')
    plt.plot(history.history['val_loss'], label='Perda de Validação')
    plt.title('Perda do Modelo')
    plt.xlabel('Época')
    plt.ylabel('Perda')
    plt.legend(loc='upper right')

    plt.tight_layout()
    plt.show()

plot_history(history_time_domain)
```

**Dica:**

* Experimente diferentes arquiteturas de rede neural para encontrar a melhor para seu problema.
* Ajuste os parâmetros do treinamento, como o número de épocas, para melhorar o desempenho do modelo.
* Utilize técnicas de regularização para evitar overfitting.


Treinar redes neurais para classificação de áudio é uma tarefa complexa, mas recompensadora. Ao praticar e experimentar, você irá adquirir habilidades importantes para trabalhar com aprendizado de máquina aplicado a áudio.

**Lembre-se:** A prática leva à perfeição! 

'''

conteudo = st.text_area("Conteúdo:", "Roteiro do vídeo")


prompt = f"""
Você é um criador de atividade Faça como eu fiz da Alura. Eu irei te passar o conteúdo do vídeo no qual você deve se basear para criar uma atividade faça como eu fiz. 

{conteudo}


Exemplo de como o conteúdo deve ser organizado na atividade:

{exemplo}
"""

# Adiciona um botão para executar a inferência
if st.button("Rodar Inferência"):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    response = model.generate_content(prompt)

    #st.markdown(response.text)
    st.text_area(label="Saída:", value=response.text, height=350)