"""
Fazer um programa que peça as 2 notas do aluno (P1 e P1) se
o aluno obtiver média ponderada maior ou igual a 7,5 será
aprovado. Caso contrário o programa deve pedir a terceira nota
(P3) e recalcular a média ponderada. Caso a media seja maior
que 6 o aluna será aprovado senão ficará de dp. O professor
dever entrar com o peso de cada nota para calculo da media
ponderada.
"""

resposta= 0
while resposta == 0:
    resposta1= "S"
    auxiliar=0
    while resposta1 in "Ss":
        prova1=int(input("Digite a nota da P1: "))
        prova2=int(input("Digite a nota da P2: "))
        peso1=int(input("Insira o peso da P1 para calcular a média: "))
        peso2=int(input("Insira o peso da P2 para calcular a média: "))
        media= (prova1*peso1 + prova2*peso2) / (peso1+peso2)
        if media >= 7.5:
            print (f'O aluno foi aprovado')
        else:
            prova3= int(input("Digite a nota 3: "))
            peso3=int(input("Digite o peso da P3 para somar na média : "))
            media = (prova1*peso1 + prova2*peso2 + prova3*peso3) / (peso1+peso2+peso3)
            if media > 6:
                print(f'O aluno foi aprovado!')
            else:
                print(f'O aluno foi reprovado')
        resposta1= str(input("Deseja Informar repetir o processo? (S/N) ")).upper()[0]
    resposta = 1

    
    
    

