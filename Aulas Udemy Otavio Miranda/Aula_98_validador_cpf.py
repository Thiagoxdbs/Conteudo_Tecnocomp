validacao = str(input())


def cpf(digito , quantidade_cpf):
    validacao_true_false = len(validacao) == 11
    soma_cpf = 0
    if validacao_true_false:
        for con_ in digito:
            if quantidade_cpf >= 2:
                validacao_con_ = int(con_)
                soma_cpf += validacao_con_*quantidade_cpf
                quantidade_cpf -= 1
            else:
                break
    else:
        print('Valor acima de 11 digitos, teste.')

    mult_div_10_11 = (soma_cpf*10)%11
    valor = mult_div_10_11 if mult_div_10_11 <= 9 else 0
    return valor

digito_1 = validacao[:9]
dig_1 = cpf(digito_1, 10)
print(dig_1)
digito_2 = validacao[:10]
print(cpf(digito_2, 11))
