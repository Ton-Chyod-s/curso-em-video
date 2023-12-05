soma_par = soma_terceira = maior_valor = 0
prin = [[], [], []]
for i in range(0, len(prin)):
    for linha in range(3):
        prin[i].append(int(input(f'Digite o valor para [{i}, {linha}]: ')))
print('-=' * 15)        
for lin in prin:
    for i in range(0, len(lin), 3):
        print(f'[ {lin[i]} ]', end="")
        print(f'[ {lin[i+1]} ]', end="")
        print(f'[ {lin[i+2]} ]')
print('-=' * 15)  
for lin in prin:
    for i in lin:
        if i % 2 == 0:
            soma_par += i
print(f'A soma dos valores par é {soma_par}')
for i in range(0, 3):
    soma_terceira += prin[i][2]
print(f'A soma da terceira coluna é {soma_terceira}')
for lin in prin[1]:
    if lin > maior_valor:
        maior_valor = lin
print(f'O maior valor da segunda linha é {maior_valor}')