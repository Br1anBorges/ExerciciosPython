'''
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
'''

#ENTRADA
nota=int(input("\nInforme a nota:\n"))
#PROCESSAMENTO

if nota <= 10:
    print(f'\nValor válido!\n')
else:
    while nota > 10:
        nota=int(input('Informe uma nota novamente!\n'))
        if nota <=10:
            print('\nValor valido!!\n')
        else:
            print(f'\nValor invalido, informe outro valor!\n')
    