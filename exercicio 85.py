par = list()
impar = list()
princ = []

for i in range(0,8):
    numero = int(input(f"Digite o {i}º valor: "))
    result = numero % 2
    if result == 0:
        par.append(numero)
    else:
        impar.append(numero)

princ.append(sorted(par[:]))
princ.append(sorted(impar[:]))

print(princ)


