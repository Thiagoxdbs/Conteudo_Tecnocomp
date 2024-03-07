validacao = str(input())

validacao_true_false = len(validacao) == 11

soma_cpf = 0

class cpf:
    def __init__(digito , quantidade_cpf):
        if validacao_true_false:
            for con_ in digito:
                if quantidade_cpf >= 2:
                    for multiplicacao in range(quantidade_cpf):
                        validacao_con_ = int(con_)
                        soma_cpf += validacao_con_*quantidade_cpf
                        quantidade_cpf -= 1
                        break
                else:
                    break
        else:
            print('Valor acima de 11 digitos, teste.')

        mult_div_10_11 = (soma_cpf*10)%11

        validacao_mult_div = mult_div_10_11 >= 9

        valor = mult_div_10_11 if validacao_mult_div else 0
        return soma_cpf

digito_1 = validacao[:9]
CPF = cpf(digito_1, 8)
print(cpf)

digito_2 = validacao[:10]
CPF = cpf(digito_2, 9)
print(cpf)