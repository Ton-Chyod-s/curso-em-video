from random import randint
from time import sleep
from operator import itemgetter
ranking = []
jogadas = {
    'Jogador 1 ': randint(1,6),
    'Jogador 2 ': randint(1,6),
    'Jogador 3 ': randint(1,6),
    'Jogador 4 ': randint(1,6)
}
maior_numero = 0
for num, valor in jogadas.items():
    print(f'{num} tirou {valor} no dado')
    sleep(.5)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')