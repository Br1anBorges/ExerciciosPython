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

print (f'{lista} \n O menor valor é: {min (lista)}, O maior valor é: {max(lista)}')

if varA > varB and varB > varC and varC > varD and varD > varE:
    print (f'O menor valor é: {varE}\nO maior valor é: {varA}')
elif varB > varA and varA > varC and varC > varD and varD > varE:
    print("continuar depois")