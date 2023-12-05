from pathlib import Path
import os

def linha(tamanho = 42):
    return '-' * tamanho


def leiaInt(txt):
    while True:
        num = str(input(txt))
        if num.isnumeric():
            return int(num)
        else:
            print(f"\033[0;31mERRO! Digite um número inteiro válido.\033[m")


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(*args):
    list_op = args
    cabecalho('MENU PRINCIPAL')
    for num, valor in enumerate(list_op):
        print(f'\033[034m{num+1} - {valor}\033[m')
    print(linha())
    num_op = leiaInt(f"\033[033mSua Opção: \033[m")
    return num_op


def criar(arquivo,diretorio):
    diretorio = Path(diretorio)

    if diretorio.exists():
        if f'{arquivo}.txt' not in os.listdir(diretorio):
            file = diretorio / f'{arquivo}.txt'
            file.touch()
            print(f'Arquivo {arquivo}.txt criado com sucesso!')


def ler(arquivo):
    with open(f'{arquivo}.txt','r') as person:
        arquivo = person.read()
    return arquivo


def visual_ler(arquivo):
    pessoas = ler(arquivo).split(',')
    for i in range(0,len(pessoas),2):
        try:
            print(f'{pessoas[i]:<30}{pessoas[i+1]:>3} anos')
        except:
            pass


def adicionando(txt='desconhecido',arquivo='pessoa'):
    with open(f'{arquivo}.txt','a') as person:
        person.write(f'{txt},')
    return txt


if __name__ == '__main__':
    pass
    