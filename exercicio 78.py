lista_num = []

for i in range(0,5):
    num = int(input(f'Digite o valor {i}: '))
    lista_num.append(num)

maior = max(lista_num)
menor = min(lista_num)

print(f'A lista que vc digitou foi: {lista_num}')
print(f'O maior valor da lista foi: {maior} nas posições ',end ='')
for num, valor in enumerate(lista_num):
    if valor == maior:
        print(f'{num}...', end ='')

print(f'\nO menor valor da lista foi: {menor} nas posições ',end ='')
for num, valor in enumerate(lista_num):
    if valor == menor:
        print(f'{num}...',end ='')