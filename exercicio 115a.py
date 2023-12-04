from ex115.lib.interface import *
from time import sleep

while True:
    numero = menu('Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do sistema')
    if numero == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    elif numero > 3 or numero < 0:
        print(f'\033[031mDigite uma opção válida\033[m')
    elif numero == 1:
        cabecalho(f'Opção 1')
    else:  
        cabecalho(f'Opção 2')
    sleep(.2)
