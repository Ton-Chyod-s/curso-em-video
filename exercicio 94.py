"""Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista 
com as mulheres D) Uma lista de pessoas com idade acima da média"""
formulario = []
pessoa = {}
soma_idade = 0
mulheres = []
acima_idade = []

while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo: '))
    pessoa['Idade'] = int(input('Idade: '))

    formulario.append(pessoa.copy())
    
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
    
print(f'Pessoas cadastradas {len(formulario)}')

for num, valor in enumerate(formulario):
    idade = formulario[num]['Idade']
    soma_idade += idade

print(f'A média das idades é {soma_idade / len(formulario)}')

for num, valor in enumerate(formulario):
    sexo = formulario[num]['Sexo']
    if sexo in 'Ff':
        mulheres.append(formulario[num]['Nome'])

print(f'As mulheres cadastradas foram  {mulheres}')

for num, valor in enumerate(formulario):
    if formulario[num]['Idade'] > soma_idade / len(formulario):
        acima_idade.append(valor)

print(f'Lista das pessoas que estão acima da média {acima_idade}')