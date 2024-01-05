'''
Faça um programa que leia 5 números e informe a soma e a
média dos números.
'''

lista_Numero=[]
contador=0
soma=0
for _ in range(5):
    contador+=1
    numero=int(input('Informe o número:\n'))
    lista_Numero.append(numero)
print(lista_Numero[:])

for i in lista_Numero[:]:
    soma+= i

print(soma/contador)