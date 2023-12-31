
user = list()
VALIDACAO_LOGIN = False

#Login
def cadastro_login(opcao):
    valor_cadastro_login = str(input(opcao)).upper().lstrip(" ")
    print("-"*len(opcao))
    VALIDACAO_CAD_LOG = valor_cadastro_login[0] == 'L' or valor_cadastro_login[0] == 'C' or valor_cadastro_login[0] == 'S'
    while True:
        if VALIDACAO_CAD_LOG:
            #print(VALIDACAO_CAD_LOG)
            break
        else:
            print("-"*len(opcao))
            print('\nERRO!\nDigite uma opção valida\n')
            print("-"*len(opcao))
            valor_cadastro_login = str(input(opcao)).upper().lstrip(" ")
            print("-"*len(opcao))
            VALIDACAO_CAD_LOG = valor_cadastro_login[0] == 'L' or valor_cadastro_login[0] == 'C'
    return valor_cadastro_login[0]

#Cadastrando
def cadastrando(confirmacao):
    global user
    confirmacao_cadastro = str(input(confirmacao)).upper().lstrip()
    validacao_cadastro = confirmacao_cadastro[0] == 'S'
    if validacao_cadastro:
        user.append(str(input('Nome: \n'))) #NOME
        user.append(str(input('Data de Nascimento: \n'))) #datanascimento
        user.append(str(input('CPF: \n')).strip('.')) #CPF
        logradouro = str(input('Local: \n'))
        bairro = str(input('Bairro: \n'))
        cidade = str(input('Cidade: \n'))
        estado = str(input('Estado: \n'))
        user.append(f'{logradouro} - {bairro} - {cidade}/{estado}')#ENDERECO
        user.append(str(input('Usuario: \n')))
        user.append(str(input('Senha: \n')))
        return user
    else:
        print("Voltando para o INICIO!")

while True:
    opcao_cad_log = cadastro_login("Digite uma opção:\n \n[L]OGIN \n[C]adastro \n[S]air\n\n --> ")
    cadastro = opcao_cad_log == 'C' 
    login = opcao_cad_log == 'L'
    sair = opcao_cad_log == 'S' 
    if cadastro:
        user = cadastrando('Deseja criar uma conta nova? \n')
        print(user)
        continue
    elif login:
        while True:
            login_user = str(input('Digite seu Usuario: \n'))
            senha_user = str(input('Digite sua Senha: \n'))
            if len(user) > 0:
                VALIDACAO_LOGIN = user[-1] == senha_user and user[-2] == login_user
            if VALIDACAO_LOGIN:
                break
            else:
                print('Usuario ou senha incorretos!')
                continuar = str(input('Quer tentar novamente: \n')).upper().lstrip(' ')
                if continuar == 'S':
                    continue
                else:
                    break
    elif VALIDACAO_LOGIN:
        break
    elif sair:
        break

print('FIM')


    


        
