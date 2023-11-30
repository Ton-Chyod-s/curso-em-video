def área(larg, comp):
    res = larg*comp
    return print(f'A área de um terreno {larg}x{comp} é de {res}m².')

def titulo(txt):
    print(txt)
    print('-' * 22)


titulo('Controle de Terrenos')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura,comprimento)
print()
