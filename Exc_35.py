'''
Escreva um programa que leia dois números e que pergunte
qual operação você deseja realizar. Você deve poder calcular
soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o
resultado da operação solicitada
'''

def aviso():
    mensagem= 'Atenção!!! \nO sistema idêntifica o valor menor do maior, e só faz operações de subtração e divisão do número maior para o menor\nNão se esqueça dos assentos!\n\n'   
    return (mensagem)


print (aviso())

valor_1= int (input("Informe o primeiro valor: "))
valor_2= int (input("Informe o segundo valor: "))
operacao=str (input("Qual é a operação desejada? "))

match operacao:
    case "soma" :
        print (f'A soma do {valor_1} + {valor_2} é: {valor_1+valor_2}')
    case "subtração":
        if valor_1 > valor_2:
            print(f'A subtração do {valor_1} - {valor_2} é: {valor_1-valor_2}')
        else:
            print (f'A subtração do {valor_2} - {valor_1} é: {valor_2-valor_1}') 
    case "multiplicação":
            print (f'A multiplicação do {valor_1} x {valor_2} é: {valor_1*valor_2}')
    case "divisão":
        if valor_1 > valor_2: 
             print(f'A divisão do {valor_1} / {valor_2} é: {valor_1/valor_2}')
        else:
             print(f'A divisão do {valor_2} / {valor_1} é: {valor_2/valor_1}')