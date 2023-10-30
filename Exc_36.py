'''
Escreva um programa para aprovar o empréstimo bancário
para compra de uma casa. O programa deve perguntar o valor da
casa a comprar, o salário e a quantidade de anos a pagar. O valor
da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a
comprar dividido pelo numero de meses a pagar.
'''

imovel= float(input("Qual é o valor do imóvel?\n "))
salario=float(input("Qual é o valor do seu salário? \n"))
anos=int(input("Quantos anos a pagar? \n"))
prestacao = imovel/(12*anos)

if prestacao > (0.30*salario):
    print("Empréstimo Negado!")
elif prestacao < (0.30*salario):
    print("Empréstimo Aprovado!")
