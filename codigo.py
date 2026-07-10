# PASSO A PASSO DO SEU PROGRAMA (Algoritmo)
# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos

# instalação do pacote "pyautogui" (pacote resposãvel pela automação das tarefas)
# comando "pip install pyautogui"

import pyautogui # TELG000821   LG  Televisao 1 820.0   172.2   2pacote responsável por automatizar tarefas do computadors
import time # pacote responsável por fazer pausas no código

# COMANDOS BÁSICOS DO PACOTE "pyautogui"
# pyautogui.click() # clica
# pyautogui.write() # escreve o usuário
# pyautogui.press() # aperta a tecla tab
# pyautogui.hotkey() # aperta um atalho de teclado

pyautogui.PAUSE = 1 # pausa de 1 segundo entre os comandos

LINK = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # URL do sistema da empresa

# PASSO 1: Entrar no sistema da empresa
pyautogui.press('win') # aperta a tecla "windows"

pyautogui.write('chrome') # escreve o nome do sistema

pyautogui.press('enter') # aperta a tecla "enter"

pyautogui.press('tab') # aperta a tecla "tab"

pyautogui.press('enter') # aperta a tecla "enter"

pyautogui.write(LINK) # escreve o URL do sistema

pyautogui.press('enter') # aperta a tecla "enter"


# PASSO 2: Fazer login

pyautogui.click(x=906, y=469) # clica na posição (906, 469) campo email

pyautogui.write("pythonimpressionador@gmail.com") # escreve o usuário

pyautogui.press('tab') # aperta a tecla "tab" campo senha

pyautogui.write("senha123") # escreve a senha

pyautogui.press('tab') # aperta a tecla "tab"

pyautogui.press('enter') # aperta a tecla "enter"

time.sleep(3) # pausa de 3 segundos para o sistema abrir


# PASSO 3: Abrir a base de dados pythonimpressionador@gmail.com(importar arquivo .csv)
# pip install pandas openpyxl
import pandas as pd # pacote responsável por manipular arquivos .csv e .xlsx
import os # pacote responsável por manipular caminhos de arquivos

caminho_arquivo = os.path.dirname(__file__) # pega o caminho do arquivo atual
caminho_produtos = os.path.join(caminho_arquivo, "produtos.csv") # cria o caminho completo do arquivo .csv

tabela = pd.read_csv(caminho_produtos) # lê o arquivo .csv e cria uma tabelas

print(tabela) # imprime a tabelas
    

# PASSO 4: Cadastrar todos os produtos
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=793, y=318)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim