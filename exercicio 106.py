def ajuda():
    cabecalho = 'SISTEMA DE AJUDA PyHELP'
    print('-=' * len(cabecalho))
    print(cabecalho)
    print('-=' * len(cabecalho))
    txt = str(input('Digite uma biblioteca ou função: '))
    return txt

ajuda()