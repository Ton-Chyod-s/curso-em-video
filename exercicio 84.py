"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
pessoas = []

while True:
    nome = str(input("None: "))
    peso = int(input("Peso: "))
    cancelar = str(input("Deseja continuar? [S/N]"))
    if cancelar in 'Nn':
        break
    pessoas.append(nome)
    pessoas.append(peso)
    
print(pessoas)
