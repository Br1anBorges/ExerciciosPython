'''
Faça um programa que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário, mostrando uma
mensagem de erro e voltando a pedir as informações.
'''

#ENTRADA

auxiliar=0
#PROCESSAMENTO

while auxiliar == 0:
        usuario=str(input("Digite seu usuário:\n"))
        senha=str(input('Digite sua senha:\n'))

        if usuario != senha:
                print('\nUsuario cadastrado\n')
                auxiliar=1
        else:
            print('\nERRO!!! NÃO É POSSIVEL CADASTRAR USUARIO E SENHA IGUAIS!\n')
        