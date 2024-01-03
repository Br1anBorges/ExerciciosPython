'''
Elaborar um programa que leia três valores para os lados de
um triângulo, considerando lados com A, B e C. Verificar se os
lados fornecidos formam um triângulo, e se for esta condição
verdadeira, deve ser indicado o tipo de triângulo formado:
isósceles, escaleno ou equilátero.
Dicas: A<B+C e B<A+C e C<A+B
'''
#ENTRADA

ladoA=int(input("\nQual o valor do lado A?\n"))
ladoB=int(input("\nQual o valor do lado B?\n"))
ladoC=int(input("\nQual o valor do lado C?\n"))

trianguloEquilatero= ladoA == ladoB and ladoA==ladoC
trianguloIsosceles= (ladoA>ladoB and ladoB==ladoC) or (ladoB>ladoA and ladoA==ladoC) or (ladoC>ladoA and ladoA==ladoB)
#PROCESSAMENTO

if trianguloEquilatero == True:
    print (f'\nO triângulo formado, é o triângulo Equilatero\n')
elif trianguloIsosceles == True:
    print (f'\nO triângulo formado, é o triângulo Isósceles\n')
else:
    print (f'\nO triângulo formado, é o triângulo Escaleno\n')
