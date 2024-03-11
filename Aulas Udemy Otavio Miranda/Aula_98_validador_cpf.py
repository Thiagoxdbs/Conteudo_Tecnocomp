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


dig_1 = cpf(validacao[:9], 10)
dig_2 = cpf(validacao[:10], 11)

task_cpf_def = f'{validacao[:9]}{dig_1}{dig_2}'

task_cpf_resultado = "CPF VALIDO" if task_cpf_def == validacao else "CPF INVALIDO"

print(task_cpf_resultado)


