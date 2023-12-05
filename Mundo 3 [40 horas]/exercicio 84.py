"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas. OK
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input("None: ")))
    temp.append(int(input("Peso: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] >maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    cancelar = str(input("Deseja continuar? [S/N] "))
    if cancelar in 'Nn':
        break

print(f'Existe {len(princ)} pessoas cadastradas!')
print(f'o maior peso foi de {maior}KG. foi de ',end='')
for linha in princ:
    if linha[1] == maior:
        print(f'{linha[0]}')

print(f'O menor peso foi de {menor}KG. foi de ',end='')
for linha in princ:
    if linha[1] == menor:
        print(f'{linha[0]}')