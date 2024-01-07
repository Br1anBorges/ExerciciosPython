'''
Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem
'''

base=int(input('Informe o primeiro número:\n'))
expoente=int(input('Informe o segundo número:\n'))
auxiliar = base
for conta in range(1, expoente):
    base+= base*expoente
print ('O primeiro número {} elevado ao segundo número {}, é = {}'.format(auxiliar,expoente,base))