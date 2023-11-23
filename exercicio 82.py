lista_num = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Digite um numero: '))
    lista_num.append(num)
    cancelar = str(input('Deseja continuar? [S/N] '))
    if cancelar in 'Nn':
        break

for i in lista_num:
    result = i % 2
    if result == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print(f'lista total: {lista_num}')
print(f'lista PAR: {lista_par}')
print(f'lista IMPAR: {lista_impar}')