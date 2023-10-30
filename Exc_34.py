'''
Escreva um programa que calcular a categoria de um produto e
determine o preço pela tabela: Categoria 1 valor de R$ 10,00;
Categoria 2 valor de R$ 15,00; Categoria 3 valor de R$ 19,00;
Categoria 4 valor de R$ 23,00 e Categoria 5 valor de R$ 27,00.
'''

categoria=int(input("Informe a categoria desejada: "))
valor=float
match categoria:
    case 1:
        valor=10.00
        print (valor)
    case 2:
        valor=15.00
        print(valor)
    case 3:
        valor=19.00
        print(valor)
    case 4:
        valor=23.00
        print(valor)
    case 5:
        valor=27.00
        print(valor)