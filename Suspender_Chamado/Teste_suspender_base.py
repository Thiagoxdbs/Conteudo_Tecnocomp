from pynput.keyboard import Key, Controller as KeyboardController #CONTROLE DO MOUSE/TECLADO
from pynput.mouse import Button, Controller as MouseController #CONTROLE DO MOUSE/TECLADO
from pynput.keyboard import Key #CONTROLE DO MOUSE/TECLADO
from selenium import webdriver #NAVEGADOR
from selenium.webdriver.support import expected_conditions #NAVEGADOR
from selenium.webdriver.common.by import By #NAVEGADOR
from selenium.webdriver.common.keys import Keys #NAVEGADOR
from selenium.webdriver.chrome.service import Service #NAVEGADOR
from webdriver_manager.chrome import ChromeDriverManager #NAVEGADOR
from selenium.webdriver.chrome.options import Options #NAVEGADOR
import requests #REQUESTS PARA INTEGRAÇÃO DO CHROMEDRIVE COM PYTHON
import time #BIBLIOTECA AUXILIAR PARA EXECUÇÃO DE TEMPO PARA O NAVEGADOR CARREGAR OS DADOS DA PAGINA
from docx import Document #AUXILIAR PARA MANIPULAÇÃO DE TEXTO
import aspose.words as aw #MANIPULAÇÃO DE TIPOS DE ARQUIVOS WORD,PDF E ETEC
from selenium.webdriver.chrome.service import Service #NAVEGADOR
from webdriver_manager.chrome import ChromeDriverManager #NAVEGADOR
import pyautogui # Print

#ATUALIZA O CHROMEDRIVE PARA VERSÃO REQUISITADA
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


#local do arquivo Chrome drive Versão 14.0 ou deixar a varialvel service atualizar
driver = webdriver.Chrome()
#Chamando o navegador
driver.get("https://moriah.qualitorsoftware.com/login.php")


#Variavel com o css selector do usuario
xpath_usu = "#cdusuario"
campo_usuario = driver.find_element("css selector", xpath_usu)
#Preenchendo o login
campo_usuario.send_keys("thiago.asouza")

time.sleep(3)

#Criar campo para clicar fora, tem bloquei se não digitar a senha.
#Variavel com o css xpath da senha
css_selector_senha = "/html/body/div[3]/form/div[1]/div[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div[2]/table/tbody/tr[4]/td/span/input"
campo_senha = driver.find_element("xpath", css_selector_senha)
campo_senha.click()
campo_senha.click()
campo_senha.click()
#Preenchendo a senha
campo_senha.send_keys("Thiagolm34.")


time.sleep(1)

#Clicando no botao de entrar
#variavel do botao entrar
bt_entrar = "/html/body/div[3]/form/div[1]/div[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div[2]/table/tbody/tr[9]/td/button"
#definindo elemento
clicar_entrar =  driver.find_element("xpath", bt_entrar)
#Click
clicar_entrar.click()

time.sleep(3)

#Abrindo pagina de pesquisa
pesquisa_xpath = "/html/body/div[1]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div[2]/div/table/tbody/tr/td/div[2]"
click_pesquisa = driver.find_element("xpath" , pesquisa_xpath).click()

time.sleep(10)

#HABILITA O PYTHON MEXER O POSICIONAMENTO OU MEXER O MOUSE
mouse = MouseController()
mouse.position = (1030, 697)
mouse.click(Button.left)
mouse.position = (530, 604)
time.sleep(2)
mouse.click(Button.left, 2)
time.sleep(2)
mouse.click(Button.left, 2)

time.sleep(4)

#HABILITA O PYTHON MEXER O POSICIONAMENTO OU MEXER O TECLADO
keyboard = KeyboardController()

#FOR PARA AUXILIAR A DIGITAR TEXTO 
for char in "Admissão":
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(0.12)
	
time.sleep(4)

#CLICLANDO EM PESQUISAR	
mouse.position = (505, 673)
mouse.click(Button.left, 2)

time.sleep(10)

#SCREENSHOT DA PAGINA PARA CAPTURAR O CONTEUDO
screen = pyautogui.screenshot()
screen.save('C:/Fotos/admissao.png')

# carregar arquivo de texto
doc = aw.Document(f"https://moriah.qualitorsoftware.com/html/index.php?_portal_=T")

# salvar texto como TXT para manipulação dos dados
doc.save(f"teste.txt")

#ABRINDO TEXTO SALVOS EM TXT DA IMAGEM PNG "DÁ SCREENSHOT"
with open(f"teste.txt" , "r" , encoding="utf-8") as conteudo:
	texto = conteudo.readlines()

#VALIDAÇÃO SÉ Á ADMISSÃO PARA SER FEITA
if "Ronda Geral" in texto:

	print("Admissão foi suspensa")
else:
	print("Não á Admissão para ser feita")

#abrindo uma nova pagina na web
#driver.execute_script("window.open()")

#time.sleep(2)
#trocando a aba
#driver.switch_to.window(driver.window_handles[1])

# Carrega a nova aba
#driver.get(f'https://moriah.qualitorsoftware.com/html/hd/hdchamado/cadastro_chamado.php?cdchamado={NumChamado}')
