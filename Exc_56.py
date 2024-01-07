'''
Altere o programa anterior para mostrar no final a soma dos
números
'''

numero1=int(input('Informe o primeiro número:\n'))
numero2=int(input('Informe o segundo número:\n'))

soma=0
if numero1 < numero2:
    for numero in range(numero1, numero2+1):
        soma += numero
        print(soma)
else:
    for numero in range(numero1,numero2-1,-1):
        soma+= numero

print('A soma do {} ao número {} é: {}'.format(numero1,numero2,soma))