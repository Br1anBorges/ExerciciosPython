'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada
de qualquer número inteiro entre 1 a 10. O usuário deve informar
de qual numero ele deseja ver a tabuada. A saída deve ser
conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
a. 5 X 10 = 5
'''

numero_Tabuada= int (input('Qual tabuada deseja consultar?\n'))
auxiliar=0
for numero in range(0,11):
    auxiliar = numero * numero_Tabuada
    print('{} x {} = {}'.format(numero_Tabuada, numero,auxiliar))