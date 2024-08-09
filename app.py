from taipy.gui import Gui
from math import cos, exp

url_exemplo = "https://github.com/taipy/taipy/blob/develop/README.md"

page = """

# Atividade referências

Copie e cole o link da referência no campo de texto:

<|{url_exemplo}|input|>


"""

def on_change(state,var_name, var_value):
    if var_name == "url_exemplo" and var_value == "Reset":
        state.url_exemplo = ""
        return

if __name__ == "__main__":
    Gui(page).run(title="Ferramentas Allan",debug=True)