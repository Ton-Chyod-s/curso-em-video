formulario = []
pessoa = {}
soma_idade = 0
mulheres = []
acima_idade = []


pessoa['Nome'] = str(input('Nome: '))
while True:
    pessoa['Sexo'] = str(input('Sexo: [M/F]'.upper()[0]))
    if pessoa['Sexo'] in 'M/F':
        break
    print('ERRO! Por favor, digite apenas M ou F.')

pessoa['Idade'] = int(input('Idade: '))

formulario.append(pessoa.copy())
while True:
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
    print('ERRO! Responda apenas S ou N.')

    if continuar == 'S':
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

print(f'As mulheres cadastradas foram ',end=' ')
for valor in mulheres:
    print(valor, end=',')
print()

for num, valor in enumerate(formulario):
    if formulario[num]['Idade'] > soma_idade / len(formulario):
        acima_idade.append(valor)

print(f'Lista das pessoas que estão acima da média')
for valor in acima_idade:
    for num, valor in valor.items():
        print(f'{num} = {valor}', end='; ')
    print()

print('FINALIZADO!!')   