 
import pyautogui
import time


pyautogui.PAUSE = 1 # -> define o tempo de espera a cada comando(função que aplica a todo programa)

# pyautogui.click -> clicar
# pyautogui.press -> precionar uma tecla
# pyautogui.write -> escrever
#pyautogui.hotkey -> atalho de teclado (ctrl, C)

# passo 1: abrir o sistema da empresa 

# abrir o googel chrome
# aperta a tecla windows
pyautogui.press("win")

# digitar o texto chome
pyautogui.write("chome")

# aperta enter
pyautogui.press("enter")

# escolher uma usuario gmail
pyautogui.click(x=768, y=619)
pyautogui.click(x=1221, y=53)
 
# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login ")
pyautogui.press("enter")

# pedir para p computador espera 3 segundos(especifico para essa linha de comando)


# passo 2: fazer o login 
pyautogui.click(x=763, y=510)
pyautogui.write("gustavocazumba1211@gmail.com")

pyautogui.press("tab")
pyautogui.write("123456789")

pyautogui.press("tab")
pyautogui.press("enter")

# passo 3: importa a base de dados do produto  

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)


time.sleep(2)
# passo 4: cadastra 1 produto


for linha in tabela.index: # executa a repetição  para a linha que tiver em TAB
      pyautogui.click(x=963, y=367)

      # codigo
      codigo = tabela.loc[linha, "codigo"]
      pyautogui.write(codigo)# clica no 1 campo
      pyautogui.press("tab")

      # marca
      marca = tabela.loc[linha, "marca"]
      pyautogui.write(marca)
      pyautogui.press("tab")

      # tipo
      tipo = tabela.loc[linha, "tipo"]
      pyautogui.write(tipo)
      pyautogui.press("tab")

      # categoria
      categoria = tabela.loc[linha, "categotia"]
      pyautogui.write(str(categoria))
      pyautogui.press("tab")

      # preco_unitariedade  
      preco_unitario = tabela.loc[linha, "preco_unitario"]
      pyautogui.write(str(preco_unitario))
      pyautogui.press("tab")

      # custo
      custo =tabela.loc[linha, "custo"]
      pyautogui.write(str(custo))
      pyautogui.press("tab")

      # obs
      obs =  str(tabela.loc[linha, "obs"])
      if obs != "nam":
             pyautogui.write(obs)
      pyautogui.press( "tab")
      pyautogui.press("enter") # apertar o botão de enviar 

      # numero positivo = scroll para cima
      # numero negativo da o scroll para baixo
      pyautogui.scroll(10000) # ->define se pagina vai subir ou descer

# passo 5: repetir o passo 4 até acabar todos os produto




