def aumentar(num,aumentar,formato=False):
    res = num + (num * aumentar/100)
    return res if formato is False else moeda(res)


def diminuir(num,diminuir,formato=False):
    res = num - (num * diminuir/100)
    return res if formato is False else moeda(res)


def dobro(num,formato=False):
    res = num * 2
    return res if formato is False else moeda(res)


def metade(num,formato=False):
    res = num / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>1.2f}'.replace('.',",")


def resumo(num,mais,menos):
    print('~' * 33)
    print(f'{"RESUMO DO VALOR".center(33)}')
    print('~' * 33)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'{mais}% de aumento: \t{aumentar(num,mais,True)}')
    print(f'{menos}% de redução: \t{diminuir(num,menos,True)}')
    print(f'Dobro do preço: \t{dobro(num,True)}')
    print(f'Metade do preço: \t{metade(num,True)}')
    print('~' * 33)