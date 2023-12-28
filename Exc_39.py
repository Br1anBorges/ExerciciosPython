'''
Elaborar um programa que leia leia um valor inteiro qualquer e
apresente este valor somente se for divisivel por 2 ou somente se
for divisivel por 3. Caso contrario não faca nada. Em hipotese
alguma este valor deve ser exibido
'''
import random

valor = random.randint(0,1000)
resto = valor 
if resto == 0:
    print (f'O número {valor} é divisivel por 2')
