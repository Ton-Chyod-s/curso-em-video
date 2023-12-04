def linha(tamanho = 42):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


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
    #criar('Klayton','pessoas')
    adicionando('i','pessoas')
    #arquivo = ler('pessoas').split(',')
    