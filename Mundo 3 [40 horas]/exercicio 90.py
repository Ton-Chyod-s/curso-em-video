situacao = {}
situacao['Nome'] = str(input('Nome: '))
situacao['Média'] = float(input(f'Média do {situacao["Nome"]}: '))

if situacao['Média'] >= 7:
    situacao['Situação'] = 'Aprovado'
elif situacao['Média']  <= 3:
    situacao['Situação'] = 'Reprovado'
else:
    situacao['Situação'] = 'Recuperação'
    
print('-=' * 20)
for num, valor in situacao.items():
    print(f'- {num} é igual a {valor}')