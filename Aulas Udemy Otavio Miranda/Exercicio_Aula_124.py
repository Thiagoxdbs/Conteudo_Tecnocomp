# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador = 0

for pergunta in perguntas:
    valor = False
    print(pergunta["Pergunta"])
    print()

    for i, opcao in enumerate(pergunta["Opções"]):
        print(f'{i})',opcao)
    resposta = input('Qual sua resposta: ')
    if resposta.isdigit():
        resposta = int(resposta)
        valor = pergunta["Resposta"] == pergunta['Opções'][resposta]
        print()
    
    if valor:
        print('Acertou!')
        print()
        contador += 1
        continue

    print("Errou")
    print()

print(f"Você acertou {contador}")