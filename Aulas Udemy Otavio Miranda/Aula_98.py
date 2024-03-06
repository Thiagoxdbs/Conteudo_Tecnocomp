validacao = str(input())

validacao_true_false = len(validacao) == 11

soma_cpf = 0
cont_ = 10

if validacao_true_false:
    for con_ in validacao:
        if cont_ >= 2:
            for multiplicacao in range(9):
                print(con_)
                print(cont_)
                validacao_con_ = int(con_)
                soma_cpf += validacao_con_*cont_
                cont_ += -1
                break
        else:
            break
else:
    print('teste')

print(soma_cpf)