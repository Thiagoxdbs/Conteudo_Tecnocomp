def xp_jogador(xp): 
    FERRO = xp < 1000
    BRONZE = xp >= 1001 and xp <= 2000
    PRATA_OURO = xp >= 2001 and xp <= 5000
    PLATINA_DIAMANTE = xp >= 5001 and xp <= 8000
    ASCENDENTE = xp >= 8001 and xp <= 9000
    IMORTAL = xp >= 9001 and xp <= 10000
    RADIANTE = xp >= 10001

    #Se XP for menor do que 1.000 = Ferro
    if FERRO:
        print(f"HEROI {nome} = Ferro")
    #Se XP for entre 1.001 e 2.000 = Bronze
    elif BRONZE:
        print(f"HEROI {nome} = Bronze")
    #Se XP for entre 2.001 e 5.000 = Prata Ouro
    elif PRATA_OURO:
        print(f"HEROI {nome} = Prata Ouro")
    #Se XP for entre 5.001 e 8.000 = Platina Diamante
    elif PLATINA_DIAMANTE:
        print(f"HEROI {nome} = Platina Diamante")
    #Se XP for entre 8.001 e 9.000 = Ascendente
    elif ASCENDENTE:
        print(f"HEROI {nome} = Ascendente")
    #Se XP for entre 9.001 e 10.000 = Imortal
    elif IMORTAL:
        print(f"HEROI {nome} = Imortal")
    #Se XP for maior ou igual a 10.001 = Radiante
    elif RADIANTE:
        print(f"HEROI {nome} = Radiante")

nome = input('Qual o nome do HEROI?\n')
while True:
    try:
        xp = int(input(f"Quanto XP possuí o Heroi {nome}?"))
    except:
        print("ERRO!\nInforme um numero.")
    xp_jogador(xp)
    validacao = input(f'Deseja informa uma nova quantidade de XP?\n').lstrip(" ").upper()
    validacao_task = validacao[0] !='S'
    if validacao_task:
        break