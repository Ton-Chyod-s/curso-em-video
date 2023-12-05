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
