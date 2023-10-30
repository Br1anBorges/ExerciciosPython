'''
Escreva um programa que calcule o preço a pagar pelo
fornecimento de energia elétrica. Pergunte a quantidade de kWh
consumida e o tipo de instalação: R para residencial, I para
industrial e C para comércios. Calcule o preço a pagar de acordo
com a tabela a seguir:
a. ● Residencial: Até 500 kWh - R$ 0,40 e acima de 500
kWh - R$ 0,65.
b. ● Comercial: Até 1000 kWh - R$ 0,55 e acima de 1000
kWh - R$ 0,60.
c. ● Industrial: Até 5000 kWh - R$ 0,55 e acima de 5000
kWh - R$ 0,60
'''

energia=float(input("Quantos Kwh consumidos? "))
tipo= str (input("R - RESIDENCIAL \nI - INDUSTRIA \nC - COMERCIO \n"))

match tipo :
    case "R":
        if energia <= 500:
            valor_Energia= 0.40*energia
            print(valor_Energia)
        else:
            valor_Energia=0.65*energia
            print(valor_Energia)
    case "r":
        if energia <= 500:
            valor_Energia= 0.40*energia
            print(valor_Energia)
        else:
            valor_Energia=0.65*energia
            print(valor_Energia)            
    case "I":
        if energia <= 5000:
            valor_Energia= 0.55*energia
            print(valor_Energia)
        else:
            valor_Energia=0.60*energia
            print(valor_Energia)
    case "i":
        if energia <= 5000:
            valor_Energia= 0.55*energia
            print(valor_Energia)
        else:
            valor_Energia=0.60*energia
            print(valor_Energia)
    case "C":
        if energia <= 1000:
            valor_Energia= 0.55*energia
            print(valor_Energia)
        else:
            valor_Energia=0.60*energia
            print(valor_Energia)
        print(valor_Energia)
    case "c":
        if energia <= 1000:
            valor_Energia= 0.55*energia
            print(valor_Energia)
        else:
            valor_Energia=0.60*energia
            print(valor_Energia)
        print(valor_Energia)