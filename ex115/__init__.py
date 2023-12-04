from ex115.lib.interface import *
from time import sleep

def menu(um,dois):
    """

    """
    while True:
        try:
            list_op = []
            cabecalho('MENU PRINCIPAL')
            list_op.append('Ver pessoas cadastradas')
            list_op.append('Cadastrar nova Pessoa')
            list_op.append('Sair do sistema')
            for num, valor in enumerate(list_op):
                print(f'\033[034m{num+1} - {valor}\033[m')
            print('-' * 35)
            numero_op = int(input(f"\033[033mSua Opção: \033[m"))
        except ValueError:
            print(f'\033[031mERRO! digite um número inteiro válido\033[m')
        else:
            if numero_op == 3:
                cabecalho('Saindo do sistema... Até logo!')
                break
            elif numero_op > 3 or numero_op < 0:
                print(f'\033[031mDigite uma opção válida\033[m')
            elif numero_op == 1:
                cabecalho(f'Opção 1')
                um
            else:  
                cabecalho(f'Opção 2')
                dois
        sleep(.2)
        
if __name__ == '__main__':
    menu('1','2')