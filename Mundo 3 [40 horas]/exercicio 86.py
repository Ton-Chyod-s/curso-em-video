"""Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e
preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a 
formatação correta."""

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