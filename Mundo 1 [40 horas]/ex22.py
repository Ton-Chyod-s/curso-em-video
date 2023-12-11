nome = str(input('Digite seu nome completo: '))
print(f'Nome Maiuscula: {nome.upper()}\nNome minuscula: {nome.lower()}')
print(f'Quantidade de letras: {len(nome.replace(" ","") )}')
print(f'Quantidade de letras do primeiro nome: {len(nome.split()[0])}')