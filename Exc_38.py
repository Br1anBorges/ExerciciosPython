'''Elaborar um programa que efetue a entrada dos valores de
medida de três pesos aferidos de forma aleatória. O programa
deve mostrar o maior peso fornecido. (com operadores lógicos
(not and or)'''

import random

medida1= random.randint(0,100)
medida2 =random.randint (0,100)
medida3 = random.randint (0,100)
print (medida1, medida2, medida3)

resultado = medida1 > medida2 and medida1 > medida3
print (resultado)
'''if medida1 > medida2 and  medida1 >medida3:
    print (medida1)
elif medida2> medida1 and medida2 > medida3:
    print (medida2)
else:
    print (medida3)'''