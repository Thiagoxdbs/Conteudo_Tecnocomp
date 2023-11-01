from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pynput import mouse, keyboard
import time
from zipfile import ZipFile  # Usei para descompactar
import requests  # Usei para receber o link da URL, fiz um input para receber mais de um link
import csv  # Usei para receber o arquivo csv e importar o conteúdo para um biblioteca e depois para uma lista
import requests
from pathlib import Path
import glob
import pandas as pd
import time
from pypdf import PdfReader
from tabula import read_pdf
import PyPDF2
from PyPDF2 import PdfReader
import aspose.words as aw
import getpass
from docx import Document
from random import choice
import string

NumChamado = "13926"

# carregar arquivo de texto
doc = aw.Document(f"C://Users/thiago.asouza/Downloads/CRIACAO_ALTERACAO_DE_ACESSOS_(NOVO)_{NumChamado}.html")

# salvar texto como HTML
doc.save(f"{NumChamado}.txt")

with open(f"{NumChamado}.txt" , "r" , encoding="utf-8") as arquivo2:
    texto = arquivo2.readlines()

#Manipulando variavel do texto do arquivo txt
if "Nome" in texto[12]:
	Nome_texto = texto[13]
	nome_split = Nome_texto.split()
	cpf_texto = texto[23]
	cpf_split = cpf_texto.split()
	cpf = cpf_split[0]

if "Nome" in texto[13]:
	Nome_texto = texto[14]
	nome_split = Nome_texto.split()
	cpf_texto = texto[24]
	cpf_split = cpf_texto.split()
	cpf = cpf_split[0]
	
if "Nome" in texto[14]:#TINHA TESTADO POR AQUI
	Nome_texto = texto[15]
	nome_split = Nome_texto.split()
	cpf_texto = texto[25]
	cpf_split = cpf_texto.split()
	cpf = cpf_split[0]

	
if "Nome" in texto[15]:
	Nome_texto = texto[16]
	nome_split = Nome_texto.split()
	cpf_texto = texto[26]
	cpf_split = cpf_texto.split()
	cpf = cpf_split[0]


if "Nome" in texto[16]:
	Nome_texto = texto[17]
	nome_split = Nome_texto.split()
	cpf_texto = texto[27]
	cpf_split = cpf_texto.split()
	cpf = cpf_split[0]
	
	
