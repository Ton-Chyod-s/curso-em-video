formulario = []
pessoa = {}
soma_idade = 0
mulheres = []
acima_idade = []
while True:
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()
        if pessoa['Sexo'] in 'M/F':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma_idade += pessoa['Idade']
    formulario.append(pessoa.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 20)
print(f'Ao total temos {len(formulario)} pessoas cadastradas.')
print(f'A média das idades é de {soma_idade / len(formulario)}')
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