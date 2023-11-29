dados = {}
gol = []

dados['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))

for i in range(partidas):
    gol.append(int(input(f'Quantos gols na partida {i}? ')))

dados['gols'] = gol[:]
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
print(f'Foi um total de {sum(gol)} gols.')