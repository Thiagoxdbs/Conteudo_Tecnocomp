validacao = str(input())

validacao_true_false = len(validacao) == 11

soma_cpf = 0
cont_ = 10

if validacao_true_false:
    for con_ in validacao:
        if cont_ >= 2:
            for multiplicacao in range(9):
                validacao_con_ = int(con_)
                soma_cpf += validacao_con_*cont_
                cont_ += -1
                break
        else:
            break
else:
    print('Valor acima de 11 digitos, teste.')

mult_div_10_11 = (soma_cpf*10)%11

validacao_mult_div = mult_div_10_11 >= 9

valor = mult_div_10_11 if validacao_mult_div else 0

print(valor)