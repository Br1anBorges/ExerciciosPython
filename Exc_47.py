'''
Faça um programa que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário, mostrando uma
mensagem de erro e voltando a pedir as informações.
'''

#ENTRADA

usuario=str(input("Digite seu usuário:\n")).upper
senha=str(input('Digite sua senha:\n')).upper

#PROCESSAMENTO

if usuario == senha:
    while usuario == senha:
        print('!!!ERRO!!!\nInforme novamente o usuário e a senha:\n')
        usuario=str(input("Digite seu usuário:\n")).upper
        senha=str(input('Digite sua senha:\n')).upper  
else:
    print('Cadastrado!')