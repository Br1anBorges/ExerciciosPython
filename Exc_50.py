'''
Altere o programa anterior permitindo ao usuário informar as
populações e as taxas de crescimento iniciais. Valide a entrada e
permita repetir a operação
'''



resposta="S"
contador=0
while resposta in "S":
    pais_A=int(input('Informe a quantidade de população do País A:\n'))
    pais_B=int(input('Informe a quantidade de população do País B:\n'))
    taxa_Pais_A=float(input('Qual é a taxa de crescimento do país A?\n'))
    taxa_Pais_B=float(input('Qual é a taxa de crescimento do país B?\n'))

    if pais_A > pais_B:
        while pais_B<pais_A:
                auxiliar=1
                contador+= auxiliar+1
                pais_A= pais_A+((taxa_Pais_A/100)*pais_A)
                pais_B=pais_B+((taxa_Pais_B/100)*pais_B)
    else: 
         while pais_A<pais_B:
                auxiliar=1
                contador+= auxiliar+1
                pais_A= pais_A+((taxa_Pais_A/100)*pais_A)
                pais_B=pais_B+((taxa_Pais_B/100)*pais_B)


    resposta=str(input('Deseja repetir a operação? [S/N]\n')).strip().upper()[0]



print('Vai levar {} anos para ultrapassar a população'.format(contador))