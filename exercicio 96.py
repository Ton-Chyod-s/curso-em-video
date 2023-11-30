def área(larg, comp):
    res = larg*comp
    return print(f'A área de um terreno {larg}x{comp} é de {res}m².')


def titulo(txt):
    print(txt)
    print('-' * 22)


while True:
    titulo('Controle de Terrenos')
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    área(largura,comprimento)
    print()
    while True:
        cancelar = str(input('Deseja cancelar? [S/N]')).upper()[0]
        if cancelar in 'SN':
            print('-- PROGRAMA FINALIZADO!! --')
            break
        print('ERRO! Digite apenas S e N.')
    if cancelar == 'N':
        break