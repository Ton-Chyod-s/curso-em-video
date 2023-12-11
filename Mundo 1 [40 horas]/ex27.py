nome = str(input('Digite seu nome completo: ')).strip().upper()
nome = nome.split()
print(f'Primeiro nome: {nome[0]}\nÚltimo nome: {nome[-1]}')