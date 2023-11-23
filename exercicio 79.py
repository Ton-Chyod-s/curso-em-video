lista_num = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista_num:
        print('Numero ja existe na lista, não da pra adicionar na lista')
    else:
        lista_num.append(num)
        print('Numero adicionado com sucesso!')

    continuar = str(input('Deseja continuar? [S/N]: '))
    if continuar.lower() == 's':
        continue
    else:
        break

print(sorted(lista_num))