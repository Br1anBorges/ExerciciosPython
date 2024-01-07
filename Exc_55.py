'''
Faça um programa que receba dois números inteiros e gere os
números inteiros que estão no intervalo compreendido por eles.
'''

numero1=int(input('Informe o primeiro número:\n'))
numero2=int(input('Informe o segundo número:\n'))

if numero1 < numero2:
    for numero in range(numero1, numero2+1):
        print(numero)
else:
    for numero in range(numero1,numero2-1,-1):
        print(numero)