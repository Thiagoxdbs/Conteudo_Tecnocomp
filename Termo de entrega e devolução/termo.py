import aspose.words as aw
from docx import Document
#import tkinter as tk #USADO PARA CRIAR A INTERFACE DO APP
import requests

q_c_u = int(input("Quantidade de usuarios que entregaram o celular: "))

banco = []

#Alex Moreira De Lima
#Backup ok
dados0 = {'Nome_Completo':'Alex Moreira De Lima'
,'CPF':'22522027859'
,'RG':'29293581-x'
,'Profissão':'Supervisor de Logística'
,'Setor':'Logistica ADM'
,'Quantidade':'1'
,'Marca_antigo':'Samsung'
,'Modelo_antigo':'Galaxy A12'
,'Marca_novo':'Samsung'
,'Modelo_novo':'Galaxy A53'
,'carregador':'Nâo'
,'IMEI_antigo':'359410827048784'
,'IMEI_novo':'350603383809362'
,'Telefone':'\(11\)978639549'
,'Obs_novo':'Aparelho entregue com carregador, cabo USB, extrator de chip, pelicula, capa de silicone e manual do usuário.'
,'Obs_antigo':'Sem carregador, está sem avaria na tela.'}

dados1 = {'Nome_Completo':'Andreza de Andrade Oliveira de Santi'
,'CPF':'20510371833'
,'RG':'273241552'
,'Profissão':'Coordenadora de Ser. Odontologico'
,'Setor':'Administração Odontológica'
,'Quantidade':'1'
,'Marca_antigo':'LG'
,'Modelo_antigo':'K10'
,'Marca_novo':'Samsung'
,'Modelo_novo':'Galaxy A53'
,'carregador':'Não'
,'IMEI_antigo':'35566909328795405'
,'IMEI_novo':'350603383816292'
,'Telefone':'(11)975985606'
,'Obs_novo':'Aparelho entregue com carregador, cabo USB, extrator de chip, pelicula, capa de silicone e manual do usuário.'
,'Obs_antigo':'Não recebeu carregador, está sem avaria na tela.'}

#Isabel Cristina Ruas de Azevedo de Oliveira
dados2 = {'Nome_Completo':'Isabel Cristina Ruas de Azevedo de Oliveira'
,'CPF':'29234463803'
,'RG':'328065195'
,'Profissão':''
,'Setor':''
,'Quantidade':''
,'Marca_antigo':''
,'Modelo_antigo':''
,'Marca_novo':''
,'Modelo_novo':''
,'carregador':''
,'IMEI_antigo':''
,'IMEI_novo':'350603383809180'
,'Telefone':'11957721389'
,'Obs_novo':''
,'Obs_antigo':''}

#Denis Martins de Carvalho
dados3 = {'Nome_Completo':'Denis Martins de Carvalho'
,'CPF':''
,'RG':''
,'Profissão':''
,'Setor':''
,'Quantidade':''
,'Marca_antigo':''
,'Modelo_antigo':''
,'Marca_novo':''
,'Modelo_novo':''
,'carregador':''
,'IMEI_antigo':''
,'IMEI_novo':''
,'Telefone':''
,'Obs_novo':''
,'Obs_antigo':''}


#Ana Neri Mulinari
#Backup ok
dados4 = {'Nome_Completo':'Ana Neri Mulinari'
,'CPF':'16353330839'
,'RG':'272465598'
,'Profissão':'Gerente Técnica Operacional'
,'Setor':'Regulamentação Médica'
,'Quantidade':'1'
,'Marca_antigo':'Samsung'
,'Modelo_antigo':'Galaxy A12'
,'Marca_novo':'Samsung'
,'Modelo_novo':'Galaxy A53'
,'carregador':'Sim'
,'IMEI_antigo':'359410827013200'
,'IMEI_novo':'350603383816003'
,'Telefone':'(11)978639525'
,'Obs_novo':'Aparelho entregue com carregador, cabo USB, extrator de chip, pelicula, capa de silicone e manual do usuário.'
,'Obs_antigo':'Devolveu com carregador, com caixa do aparelho, com capa e está sem avaria na tela.'}

#
dados5 = {'Nome_Completo':'Hugo Pêgo dos Santos'
,'CPF':'27928784874'
,'RG':'341853045'
,'Profissão':'Coordenador de Suprimentos'
,'Setor':'Compras'
,'Quantidade':'1'
,'Marca_antigo':'Samsung'
,'Modelo_antigo':'Galaxy A30s'
,'Marca_novo':'Samsung'
,'Modelo_novo':'Galaxy A53'
,'carregador':'sim'
,'IMEI_antigo':'351763114425273'
,'IMEI_novo':'350603383815609'
,'Telefone':'(11)941661878'
,'Obs_novo':'Aparelho entregue com carregador, cabo USB, extrator de chip, pelicula, capa de silicone e manual do usuário.'
,'Obs_antigo':'Devolveu sem carregador, com caixa do aparelho, com fone de ouvido, com capa e está sem avaria na tela.'}

#Eduardo Hideo Zerrenner Miyashiro
dados6 = {'Nome_Completo':'Eduardo Hideo Zerrenner Miyashiro'
,'CPF':'16357908835'
,'RG':'21314526'
,'Profissão':'Gerente de Suprimentos'
,'Setor':'Compras Csc'
,'Quantidade':'1'
,'Marca_antigo':'Motorola'
,'Modelo_antigo':'Moto G8 Power'
,'Marca_novo':'Samsung'
,'Modelo_novo':'Galaxy A53'
,'carregador':'Não'
,'IMEI_antigo':'359097108419337'
,'IMEI_novo':'350603383469233'
,'Telefone':'(11)975021938'
,'Obs_novo':'Aparelho entregue com carregador, cabo USB, extrator de chip, pelicula, capa de silicone e manual do usuário.'
,'Obs_antigo':'Devolveu sem carregador, com caixa do aparelho, com fone de ouvido, com capa e está sem avaria na tela.'}

#Carolina De Oliveira Praxedes
dados7 = {'Nome_Completo':'Carolina De Oliveira Praxedes'
,'CPF':'03528109394'
,'RG':'2002010515140'
,'Profissão':'Enfermeiro De Controle De Infecção Hospitalar'
,'Setor':'SCIH Hospital'
,'Quantidade':'1'
,'Marca_antigo':'Samsung'
,'Modelo_antigo':'Galaxy A12'
,'Marca_novo':'Samsung'
,'Modelo_novo':'Galaxy A53'
,'carregador':'Sim'
,'IMEI_antigo':'354291421142412'
,'IMEI_novo':'350603383812416'
,'Telefone':'(11)988704172'
,'Obs_novo':'Aparelho entregue com carregador, cabo USB, extrator de chip, pelicula, capa de silicone e manual do usuário.'
,'Obs_antigo':'Devolveu com carregador, com caixa do aparelho,cabo USB, extrator de chip, pelicula, com capa de silicone e está sem avaria na tela.'}

#Suzanna Isabella de Medeiros Bertoncello
dados = {'Nome_Completo':'Suzanna Isabella de Medeiros Bertoncello'
,'CPF':'33206206812'
,'RG':'348058020'
,'Profissão':'Enfermeira Referência'
,'Setor':'Internação Terreo'
,'Quantidade':'1'
,'Marca_antigo':'Samsung'
,'Modelo_antigo':'Galaxy A12'
,'Marca_novo':'Samsung'
,'Modelo_novo':'Galaxy A53'
,'carregador':'Sim'
,'IMEI_antigo':'354291421139244'
,'IMEI_novo':'350603383819593'
,'Telefone':'(11)945231273'
,'Obs_novo':'Aparelho entregue com carregador, cabo USB, extrator de chip, pelicula, capa de silicone e manual do usuário.'
,'Obs_antigo':'Devolveu com carregador, cabo USB, pelicula com pequenas avarias, com capa de silicone e está sem avaria na tela.'}

#Simone Souza da Silva
dados = {'Nome_Completo':'Simone Souza da Silva'
,'CPF':'29597549808'
,'RG':'29877981x'
,'Profissão':'Enfermeira Referencia'
,'Setor':'Unidade Ambulatorial Oncologico'
,'Quantidade':'1'
,'Marca_antigo':'LG'
,'Modelo_antigo':'K61'
,'Marca_novo':'Galaxy'
,'Modelo_novo':'A53'
,'carregador':'Sim'
,'IMEI_antigo':'354327111666243'
,'IMEI_novo':'350603383739122'
,'Telefone':'(11)991290937'
,'Obs_novo':'Aparelho entregue com carregador, cabo USB, extrator de chip, pelicula, capa de silicone e manual do usuário.'
,'Obs_antigo':'Devolveu com carregador, cabo USB, sem pelicula, com capa de silicone e está sem avaria na tela.'}


#Denis Martins de Carvalho
dados = {'Nome_Completo':'Denis Martins de Carvalho'
,'CPF':'32920515845'
,'RG':'410724853'
,'Profissão':'Gerente Contábil'
,'Setor':'Contabilidade Csc'
,'Quantidade':'1'
,'Marca_antigo':'Samgung'
,'Modelo_antigo':'Galaxy A30s'
,'Marca_novo':'Samgung'
,'Modelo_novo':'Galaxy A53'
,'carregador':'Sim'
,'IMEI_antigo':'351763114400938'
,'IMEI_novo':'350603383815286'
,'Telefone':'(11)957756098'
,'Obs_novo':'Aparelho entregue com carregador, cabo USB, extrator de chip, pelicula, capa de silicone e manual do usuário.'
,'Obs_antigo':'Devolveu com carregador, cabo USB, pelicula com pequenas avarias e está sem avaria na tela.'}

#
dados = {'Nome_Completo':''
,'CPF':''
,'RG':''
,'Profissão':''
,'Setor':''
,'Quantidade':''
,'Marca_antigo':''
,'Modelo_antigo':''
,'Marca_novo':''
,'Modelo_novo':''
,'carregador':''
,'IMEI_antigo':''
,'IMEI_novo':''
,'Telefone':''
,'Obs_novo':''
,'Obs_antigo':''}



banco.append(dados0)
banco.append(dados1)
banco.append(dados2)
banco.append(dados3)
banco.append(dados4)


print(banco)
#Abrindo arquivo que vai ser editado
def termo(arquivo):
	#Trocando caracteres no texto do word
	for c in range(0,4):
		documento = Document(arquivo)
		for paragrafo in documento.paragraphs:	
			paragrafo.text = paragrafo.text.replace("nome_t",f"{banco[c]['Nome_Completo']}")
			paragrafo.text = paragrafo.text.replace("rg_t" ,f"{ banco[c]['RG']}")
			paragrafo.text = paragrafo.text.replace("cpf_t" ,f"{ banco[c]['CPF']}")
			paragrafo.text = paragrafo.text.replace("profissao_t" ,f"{ banco[c]['Profissão']}")
			paragrafo.text = paragrafo.text.replace("unidade_t" ,f"{ banco[c]['Quantidade']}")
			paragrafo.text = paragrafo.text.replace("marca_tn" ,f"{ banco[c]['Quantidade']}")
			paragrafo.text = paragrafo.text.replace("modelo_tn" ,f"{ banco[c]['Modelo_novo']}")
			paragrafo.text = paragrafo.text.replace("telefone_t" ,f"{ banco[c]['Telefone']}")
			paragrafo.text = paragrafo.text.replace("emei_tn" ,f"{ banco[c]['IMEI_novo']}")
			paragrafo.text = paragrafo.text.replace("setor_t" ,f"{ banco[c]['Setor']}")
			paragrafo.text = paragrafo.text.replace("obs_tn" ,f"{ banco[c]['Obs_novo']}")
			paragrafo.text = paragrafo.text.replace("Marca_ta" ,f"{ banco[c]['Marca_antigo']}")
			paragrafo.text = paragrafo.text.replace("Modelo_ta" ,f"{ banco[c]['Modelo_antigo']}")
			paragrafo.text = paragrafo.text.replace("imei_ta" ,f"{ banco[c]['IMEI_antigo']}")
			paragrafo.text = paragrafo.text.replace("obs_ta"  ,f"{ banco[c]['Obs_antigo']}")
			paragrafo.text = paragrafo.text.replace("carregador_t" ,f"{ banco[c]['carregador']}")
			
			#Salvando conteudo em um novo arquivo word	
			documento.save(f"{ banco[c]['Nome_Completo']}- {arquivo}")
		print('TERMO FOI GERADO')

termo('Entrega_Smartphone.docx')
termo('Recebimento_Smartphone.docx')
