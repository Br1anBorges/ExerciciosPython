valor_1= int (input("Digite o primeiro valor: "))
valor_2= int (input("Digite o segundo valor: "))
valor_3= int (input("Digite o terceiro valor: "))


if valor_1 > valor_2 and valor_2 > valor_3:
    print (f'{valor_3} - {valor_2} - {valor_1}'2)
elif valor_1 > valor_3 and valor_3 > valor_2:
    print(f'{valor_2} - {valor_3} - {valor_1}')
elif valor_2> valor_1 and valor_1 > valor_3:
    print(f'{valor_3} - {valor_1} - {valor_2}')
elif valor_2> valor_3 and valor_3 > valor_1:
    print(f'{valor_1} - {valor_3} - {valor_2}')
elif valor_3> valor_1 and valor_1 > valor_2:
    print (f'{valor_2} - {valor_1} - {valor_3}')
elif valor_3> valor_2 and valor_2 > valor_1:
    print(f'{valor_1} - {valor_2} - {valor_3}')