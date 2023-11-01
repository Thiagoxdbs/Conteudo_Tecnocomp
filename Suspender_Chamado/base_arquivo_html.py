from docx import Document
import aspose.words as aw
from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
import time



mouse = Controller()
mouse.position = (1030, 697)
mouse.click(Button.left)
time.sleep(2)
mouse.position = (530, 604)
mouse.click(Button.left, 2)

# carregar arquivo de texto
#doc = aw.Document(f"http://www.pythonds.com.br/posts/ws.html")

# salvar texto como HTML
#doc.save(f"teste.txt")

#with open(f"teste.txt" , "r" , encoding="utf-8") as conteudo:
#	texto = conteudo.readlines()

#if "Admissão" in texto:
#	print("Admissão foi suspensa")
#else:
#	print("Não á Admissão para ser feita")