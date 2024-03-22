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
    print(pergunta["Pergunta"])
    for c in range(4):
        print(f'{c})',pergunta["Opções"][c])
    resposta = int(input('Qual sua resposta: '))
    valor = pergunta["Resposta"] == pergunta['Opções'][resposta]
    if valor:
        print('Acertou!')
        contador += 1
        continue
    print("Errou")

print(f"Você acertou {contador}")