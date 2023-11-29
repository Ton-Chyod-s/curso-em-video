from datetime import date
formulario = {}
data = date.today()

formulario['Nome'] = str(input('None: '))
nascimento = int(input('Ano nascimento: '))
formulario['Idade'] = data.year - nascimento
formulario['Carteira de trabalho'] = int(input('Carteira de trabalho (0 não tem): '))

if formulario['Carteira de trabalho'] != 0:
    formulario['Ano contratação'] = int(input('Ano contratação: '))
    formulario['Salário R$'] = float(input('Salário: '))
    formulario['Aposentadoria'] = ( formulario['Ano contratação'] + 35 ) - nascimento

print('-=' * 25)
for num, valor in formulario.items():
    print(f'{num} tem o valor {valor}')