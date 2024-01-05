'''
Faça um programa que leia 5 números e informe o maior
número.
'''

lista_Numero= []


for _ in range(5):
    numero= int (input('Informe um número:\n'))
    lista_Numero.append(numero)


print (max(lista_Numero[:]), min(lista_Numero[:]))