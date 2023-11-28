from random import randint
from time import sleep

jogada = []
print('-=' * 15)
print('       JOGADA DA MEGA SENA       ')
print('-=' * 15)
num = int(input("Digite quantos jogos serão feitos: "))
print('-=' * 3, f' SORTEANDO {num} JOGOS ', '-=' *3)
for linha in range(num):
    if len(jogada) != 0:
        jogada.clear()
    for i in range(0,6):
        numero = randint(1,60)
        if numero not in jogada:
            jogada.append(numero)
        elif numero in jogada:
            numero = randint(1,60)
            jogada.append(numero)

    print(f'Jogo {linha + 1}: {jogada}')
    sleep(.5)
print('-=' * 4,'<  BOA SORTE  >', '-=' * 4)