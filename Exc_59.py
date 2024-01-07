'''
Faça um programa que peça 10 números inteiros, calcule e
mostre a quantidade de números pares e a quantidade de
números impares
'''
lista_Numeros_Pares=[]
lista_Numeros_Impares=[]
for _ in range (10):
    numero=int(input('Informe um número:\n'))

    if numero % 2 == 0:
        lista_Numeros_Pares.append(numero)
    else:
        lista_Numeros_Impares.append(numero)
print(f'Tem: {len(lista_Numeros_Impares)} números impares, e {len(lista_Numeros_Pares)} números pares!')