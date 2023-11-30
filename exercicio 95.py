time = {}
dados = []
gol = []
contador = 0

while True:
    dados.append(str(input('Nome do jogador: ')))
    dados.append(int(input(f'Quantas partidas {dados[0]} jogou? ')))
    for i in range(dados[1]):
        gol.append(int(input(f'Quantos gols na partida {i}? ')))
    time[f'Jogador {contador}'] = dados[:]
    contador += 1
    dados.clear()
    cancelar = str(input('Deseja continuar? [S/N]')).upper()
    if cancelar == 'N':
        break

dados.append(gol[:])
print(time)

"""
dados['Total'] = sum(i for i in gol)
print('-=' * 20)
print(dados)
print('-=' * 20)
for num, valor in dados.items():
    print(f'O campo {num} tem o valor {valor}')
print('-=' * 20)
print(f'O jogador {dados["Nome"]} jogou {len("gols")} partidas.')
for num, valor in enumerate(gol):
    print(f'=> Na partida {num}, fez {valor} gols.')
print(f'Foi um total de {sum(gol)} gols.')"""