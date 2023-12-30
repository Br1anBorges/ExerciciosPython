"""
Fazer um programa que peça as 2 notas do aluno (P1 e P1) se
o aluno obtiver média ponderada maior ou igual a 7,5 será
aprovado. Caso contrário o programa deve pedir a terceira nota
(P3) e recalcular a média ponderada. Caso a media seja maior
que 6 o aluna será aprovado senão ficará de dp. O professor
dever entrar com o peso de cada nota para calculo da media
ponderada.
"""

p1= int(input("Insira a nota da P1: "))
p2= int(input("Insira a nota da p2: "))

peso= 0
while peso == 0:
    resposta= "S"
    auxiliar=0
    while resposta in "Ss":

        peso=int(input("Insira o PESO, para calcular a média ponderada"))
        auxiliar+= peso
        soma= peso*p1 + peso*p2
        media = soma/auxiliar
        if media >= 7.5:
            print (f'O aluno foi aprovado')
        elif media < 7.5:
            p3= int(input("Insira a nota da p3: "))
            soma= peso*p1 + peso*p2 + peso*p3
        else:
            print(f'O aluno foi reprovado')
        resposta= str(input("Deseja Informar mais peso? (S/N) ")).upper()[0]

    
    
    

