lista_num = []
for i in range(0,5):
    num = int(input(f'Digite o valor: '))
    if i == 0 or num > lista_num[-1]:
        lista_num.append(num)
    else:
        pos = 0
        while pos < len(lista_num):
            if num <= lista_num[pos]:
                lista_num.insert(pos, num)
                break
            pos += 1

print(lista_num)