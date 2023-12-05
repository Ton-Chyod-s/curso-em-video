lista_num = []

while True:
    num = int(input('Digite um valor: '))
    lista_num.append(num)
    cancelar = str(input('Deseja continuar? [S/N] '))
    if cancelar in 'Nn':
        break

# A) Quantos números foram digitados.
print(f'foram digitados: {len(lista_num)} elementos')
# B) A lista de valores, ordenada de forma decrescente.
print(f'ordem decrescente: {sorted(lista_num, reverse = True)}')
# C) Se o valor 5 foi digitado e está ou não na lista.
if 5 in lista_num:
    print(f'O valor 5 esta presente na lista, na posição {lista_num.index(5)}')
else:
    print('O valor 5 não esta na lista')