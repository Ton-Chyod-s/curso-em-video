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


def criar(txt,arquivo):
    with open(f'{arquivo}.txt','w') as person:
        person.write(txt)


def ler(arquivo):
    with open(f'{arquivo}.txt','r') as person:
        arquivo = person.read()
    return arquivo


def adicionando(txt,arquivo):
    with open(f'{arquivo}.txt','a') as person:
        person.write(f' {txt}')


if __name__ == '__main__':
    menu('Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do sistema')
    