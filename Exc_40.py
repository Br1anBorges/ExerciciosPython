'''
Ler cinco valores numéricos inteiros (variaveis A,B,C, D e E)
localizar e apresentar o maior e o menor valor.
'''

varA= int(input("Digite o valor de A: "))
varB= int(input("Digite o valor de B: "))
varC= int(input("DIgite o valor de C: "))
varD= int(input("Digite o valor de D: "))
varE= int(input("Digite o valor de E: "))

lista=[varA,varB,varC,varD,varE]

print (f'{lista} \n O maior valor é: {min (lista)}, O menor valor é: {max(lista)}')

auxiliar= varA > varB,varC,varD,varE and varB < varA,varC,varD, varE
print(auxiliar)