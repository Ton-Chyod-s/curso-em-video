time = []
jogador = {}
gol = []
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(partidas):
        gol.append(int(input(f'Quantos gols na partida {i}? ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    time.append(jogador.copy())
    gol.clear()
    jogador.clear()
    while True:
        cancelar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if cancelar in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if cancelar == 'N':
        break
print('-=' * 30)
print(f"{'cod':<2} {'name':<18} {'gols':<18} {'total':>5}")
print('-' * 48)
for num, valor in enumerate(time):
    print(f'{num:<3}', end=' ')
    for i, v in valor.items():
        print(f'{str(v):<18}', end=' ' )
    print()
print('-' * 48)
while True:
    mostrar = int(input('Quer mostrar os dados de qual jogador? (999 para parar) '))
    if mostrar == 999:
        print('-- VOLTE SEMPRE --')
        break
    if mostrar >= len(time):
        print(f'ERRO! Não existe jogador de código {mostrar}')
    else:
        print(F'--> LEVANTAMENTO DO JOGADOR {valor["nome"]}: ')
        for num, valor in enumerate(time[mostrar]['gols']):
            print(f'  => No jogo {num} fez {valor} gols.')
        print(f'Foi um total de {time[mostrar]["total"]} gols')