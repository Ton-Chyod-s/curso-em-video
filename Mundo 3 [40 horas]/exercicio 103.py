def ficha(nome= '<desconhecido>',gol= 0):
    nome_interno = str(input('Nome do jogador: '))
    if nome_interno != '':
        nome = nome_interno
    gol_interno = str(input('Número de Gols: '))
    if gol_interno != '':
        gol = int(gol_interno)
    return f'O jogador {nome} fez {gol} gols no campeonato.'

print(ficha())