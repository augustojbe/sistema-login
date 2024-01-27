from controller import *


while True:
    print('========= [ Menu] =========')
    decidir = int(input('Digite 1 para castrar\n'
                    'Digite 2 para logar\n'
                    'Digite 3 para sair\n'))
    
    if decidir == 1:
        nome = input('Digte seu nome')
        email = input('Digite seu email')
        senha = input('Digite sua senha')
        resultado = ControllerCadastro.cadastrar(nome, email, senha)
        
        if resultado == 2:
            print('Tamanho do nome digitado inválido')
        elif resultado == 3:
            print('email maior que 200 caracteres')
        elif resultado == 4:
            print('Tamanho da senha inválido')
        elif resultado == 5:
            print('Email ja cadastrado')
        elif resultado == 6:
            print('Erro interno do sistema')
        elif resultado == 1:
            print('Cadastrado com sucesso')
    elif decidir == 2:
        email = input('Digte seu email')
        senha = input('Digite seu senha')
        resultado = ControllerLogin.logi(email, senha)
        if not resultado:
            print('Email ou senha inválida')
        else:
            print(f'Logado....{resultado}')
    else:
        break
