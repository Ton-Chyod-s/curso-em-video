princ = [[], []]

for i in range(0,8):
    numero = int(input(f"Digite o {i}º valor: "))
    if numero % 2 == 0:
        princ[0].append(numero)
    else:
        princ[1].append(numero)
print('-=' * 30)
print(f'Os numeros pares são {sorted(princ[0])}')
print(f'Os numeros impares são {sorted(princ[1])}')
print('-=' * 30)

