'''
Elaborar um programa que leia leia um valor inteiro qualquer e
apresente este valor somente se for divisivel por 2 ou somente se
for divisivel por 3. Caso contrario não faca nada. Em hipotese
alguma este valor deve ser exibido
'''
import random

valor = random.randint(0,1000)
resto= valor%10

while valor != 0 or valor != 2 or valor != 4 or valor != 6 or valor != 8:
    auxiliar=0
    resto = valor%10
    valor= valor/10
    auxiliar= valor+resto+auxiliar
    if auxiliar == 0 or auxiliar == 2 or auxiliar == 4 or auxiliar ==6 or auxiliar == 8:
        print (f'Valor é divisivel por 3')
        break
    match resto:
        case 0: 
            print (f'É divisivel por 2')
            break
        case 2: 
            print(f'É divisivel por 2')
            break
        case 4: 
            print (f'É divisivel por 2')
            break
        case 6:
            print (f'É divisivel por 2')
            break
        case 8:
            print (f'É divisivel por 2')
            break
