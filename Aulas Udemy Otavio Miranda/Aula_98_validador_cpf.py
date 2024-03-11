import re

validacao = re.sub(
    r'[^0-9]',
    '',
    str(input()))


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

pri_char_ent = validacao[0]
pri_char_ent_rep = pri_char_ent * len(validacao)

if validacao != pri_char_ent_rep:
    dig_1 = cpf(validacao[:9], 10)
    dig_2 = cpf(validacao[:10], 11)

    task_cpf_def = f'{validacao[:9]}{dig_1}{dig_2}'

    task_cpf_resultado = f"CPF VALIDO \n {task_cpf_def}" \
        if task_cpf_def == validacao else "CPF INVALIDO\n {task_cpf_def}"

    print(task_cpf_resultado)
else:
    print('CPF INVALIDO')


