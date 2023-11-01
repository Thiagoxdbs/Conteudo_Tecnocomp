def elo_jogador(ELO): 
    FERRO = ELO < 10100
    BRONZE = ELO >= 11 and ELO <= 20
    PRATA_OURO = ELO >= 21 and ELO <= 50
    PLATINA_DIAMANTE = ELO >= 51 and ELO <= 80
    ASCENDENTE = ELO >= 81 and ELO <= 90
    IMORTAL = ELO >= 91 and ELO <= 100
    RADIANTE = ELO >= 101

    if FERRO:
        print(f"HEROI {nome} = Ferro")
    elif BRONZE:
        print(f"HEROI {nome} = Bronze")
    elif PRATA_OURO:
        print(f"HEROI {nome} = Prata Ouro")
    elif PLATINA_DIAMANTE:
        print(f"HEROI {nome} = Platina Diamante")
    elif ASCENDENTE:
        print(f"HEROI {nome} = Ascendente")
    elif IMORTAL:
        print(f"HEROI {nome} = Imortal")
    elif RADIANTE:
        print(f"HEROI {nome} = Radiante")

nome = input('Qual o nome do HEROI?\n')
while True:
    try:
        vitoria = int(input(f"Quantas VITORIAS possuí o Heroi {nome}?"))
        derrota = int(input(f"Quantas DERROTAS possuí o Heroi {nome}?"))
        ELO = vitoria - derrota
    except:
        print("ERRO!\nInforme um numero.")
    elo_jogador(ELO)
    validacao = input(f'Deseja ver um novo ELO?\n').lstrip(" ").upper()
    validacao_task = validacao[0] !='S'
    if validacao_task:
        break