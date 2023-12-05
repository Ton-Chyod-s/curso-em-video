from ex115.lib.interface import *
from time import sleep

criar('pessoa','C:/Users/User/Documents/GitHub/curso-em-video/Mundo 3 [40 horas]')
arquivo = 'pessoa'
while True:
    numero = menu('Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do sistema')
    if numero == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    elif numero > 3 or numero < 0:
        print(f'\033[031mDigite uma opção válida\033[m')
    elif numero == 1:
        cabecalho(f'Opção de listar o conteúdo de um arquivo')
        visual_ler(arquivo)
    else:  
        cabecalho(f'Novo Cadastro')
        nome = adicionando(str(input('Digite o nome: ')),arquivo)
        adicionando(leiaInt('Digite a idade: '),arquivo)
        print(f'Novo registro de {nome} adicionado.')
    sleep(.2)
