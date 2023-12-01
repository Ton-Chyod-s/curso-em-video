def aumentar(num,aumentar):
    res = num + (num * aumentar/100)
    return res


def diminuir(num,diminuir):
    res = num - (num * diminuir/100)
    return res


def dobro(num):
    res = num * 2
    return res


def metade(num):
    res = num / 2
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>1.2f}'.replace('.',",")
