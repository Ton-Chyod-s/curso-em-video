from time import sleep

c =('\033[m', # 0-sem cores
    '\033[0;30;41m', #1 - vermelho
    '\033[4;33;44m', #2 - azul
    '\033[1;35;43m', #3 - amarelo
    '\033[30;42m' #4 - verde
)

def titulo(txt, cor=0):
    cabecalho_tamanho = len(txt) + 4
    print(c[cor],end='')
    print('~' * cabecalho_tamanho)
    print(f'  {txt}')
    print('~' * cabecalho_tamanho)
    print(c[0],end='')

def ajuda():
    while True:
        titulo('SISTEMA DE AJUDA PyHELP',1)
        txt = str(input('Digite uma biblioteca ou função: ')).upper()
        if txt == 'FIM':
            titulo('ATÉ LOGO')
            break
        titulo(f'Acessando o comando {txt}',4)
        sleep(.3)
        print(c[2])
        help(txt)
        print(c[0])
        sleep(.5)


ajuda()