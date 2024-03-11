import random

validacao = ''
for gerador in range(9):
    validacao += str(random.randint(0,9))


def cpf(digito , quantidade_cpf):
    soma_cpf = 0
    for con_ in digito:
        if quantidade_cpf >= 2:
            validacao_con_ = int(con_)
            soma_cpf += validacao_con_*quantidade_cpf
            quantidade_cpf -= 1
        else:
            break

    mult_div_10_11 = (soma_cpf*10)%11
    valor = mult_div_10_11 if mult_div_10_11 <= 9 else 0
    return valor

pri_char_ent = validacao[0]
pri_char_ent_rep = pri_char_ent * len(validacao)


dig_1 = cpf(validacao[:9], 10)
dig_2 = cpf(validacao[:10], 11)

task_cpf_def = f'{validacao[:9]}{dig_1}{dig_2}'

print(task_cpf_def)
