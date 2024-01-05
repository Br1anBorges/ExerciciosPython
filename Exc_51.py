'''
Faça um programa que imprima na tela os números de 1 a 20,
um abaixo do outro. Depois modifique o programa para que ele
mostre os números um ao lado do outro
'''

lista_Numeros=[]

for numero in range(0,20,1):
    numero += 1
    lista_Numeros.append(numero)
    print(numero)
print(lista_Numeros[:])

