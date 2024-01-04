'''
Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
f. Orientação sexual L,G,B,T,Q,I,A,+
'''
nome=str(input('Qual é seu nome?\n'))
quantidade_Nome=len(nome)

while quantidade_Nome <= 3:
    nome=str(input('\nDados Incorretos, Por favor, informe nome com mais de três letras!\n'))
    quantidade_Nome=len(nome)
print ('Nome {} foi registrado com sucesso\n'.format(nome))

idade=int(input('\nInforme sua idade:\n'))

while idade > 150 or idade ==0:
    idade=int(input('Dados incorretos! Por favor, informe idade abaixo de 150 anos, e acima de 0 anos!\n'))
print ('Idade {} foi registrado com sucesso!\n'.format(idade))

salario=float(input('Qual é seu salário?\n'))
while salario <= 0:
    salario=float(input('Dados incorretos! Por favor, informe salário acima de 0!!!\n'))
print('Salário {} registrado com sucesso!\n'.format(salario))

sexo=str(input('Informe seu sexo: [M/F]')).strip().upper()[0]

while sexo not in "MF":
    sexo=str(input('Dados incorretos! Por favor, informe um sexo válido!\n')).strip().upper()[0]
print('Sexo {} registrado com sucesso!\n'.format(sexo))

estado_Civil=str(input('Informe o seu estado civil: [S , C , V , D]\n')).strip().upper()[0]

while estado_Civil not in "SCVD":
    estado_Civil=str(input('Dados incorretos, por favor, informe um estado civil válido!!!\n')).strip().upper()[0]
print('Estado civil {} registrado com sucesso!'.format(estado_Civil))

orientacao_Sexual=str(input('\nInforme sua orientação sexual: [L,G,B,T,Q,I,A,P,+]\n')).strip().upper()[0]

while orientacao_Sexual not in "LGBTQIAP+":
    orientacao_Sexual=str(input('Dados, invalidos! Por favor, informe uma sexualidade válida!\n')).strip().upper()[0]
print('Orientação Sexual {} registrada com sucesso!\n'.format(orientacao_Sexual))