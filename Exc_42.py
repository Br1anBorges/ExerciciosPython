'''
Um posto está vendendo combustíveis com a seguinte
tabela de descontos: 
até 20 litros, desconto de 3% por litro Álcool 
acima de 20 litros, desconto de 5% por litro 
até 20 litros, desconto de 4% por litro Gasolina acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros
vendidos e o tipo de combustível (codificado da seguinte
forma: A-álcool, G-gasolina), calcule e imprima o valor a
ser pago pelo cliente sabendo-se que o preço do litro da
gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90
'''
 #ENTRADA
quantos_Litros= float(input("\nQuantos litros foi vendido?\n"))
resposta = str(input("\nQual é o tipo de combustivel?\n\nA: Álcool\nG: Gasolina\n*2")).upper()
litro_Gasolina= 3.30
litro_Alcool= 2.90
preco_Gasolina=0
preco_Alcool=0
desconto=0



#PROCESSAMENTO

match resposta:
    case "A":
        if quantos_Litros <= 20:
            desconto= (litro_Alcool*quantos_Litros)*0.03
            preco_Alcool = litro_Alcool*quantos_Litros - desconto
            print(f'O valor a ser pago por {quantos_Litros} litros de álcool, é de:\n{preco_Alcool}\n')
        else:
            desconto=(litro_Alcool*quantos_Litros)*0.05
            preco_Alcool= litro_Alcool*quantos_Litros-desconto
            print(f'O valor a ser pago por {quantos_Litros} Litros de álcool, é de:\n{preco_Alcool}')
    case "G":
        if quantos_Litros <= 20:
            desconto= (litro_Gasolina*quantos_Litros)*0.04
            preco_Gasolina= litro_Gasolina*quantos_Litros - desconto
            print(f'O valor a ser pago por {quantos_Litros} Litros de gasolina, é de:\n{preco_Gasolina}\n')
        elif quantos_Litros>20 :
            desconto=(litro_Gasolina*quantos_Litros)*0.06
            preco_Gasolina=litro_Gasolina*quantos_Litros - desconto
            print(f'O valor a ser pago por {quantos_Litros} Litros de gasolina, é de:\n{preco_Gasolina}\n')
    case _: 
        print ("\nPor favor, informe uma das alternativas acima!!!\n")