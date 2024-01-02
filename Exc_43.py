'''
Ler o nome de 2 times e o número de gols marcados na
partida (para cada time). Escrever o nome do vencedor.
Caso não haja vencedor deverá ser impressa a palavra
EMPATE.
'''

#ENTRADA
import random
time1=str(input("\nInforme o nome do primeiro time:\n"))
gol_Time1=int(input(f"\nQuantos gols o {time1} fez?\n"))
time2=str(input("\nInforme o nome do segundo time:\n"))
gol_Time2=int(input(f"\nQuantos gols o {time2} fez?\n"))
vencedores= ['Matheus','Lucas','Kevin','Rafael','Laiza','Jhessy']

#PROCESSAMENTO

if gol_Time1 > gol_Time2:
    print (f"\nO vencedor é\n{time1}\nParabéns {random.choice(vencedores)}!!!")
elif gol_Time1 == gol_Time2:
    print("EMPATE!")
else: 
    print(f'\nO vencedor é:\n{time2}\nParabéns {random.choice(vencedores)}!!!')