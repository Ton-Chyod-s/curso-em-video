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


def moeda(txt):
    dinheiro = {
        'Euro' :  '€',
        'Real': 'R$',
        'Dolar':'$',
        'Libra': '£'
    }
    if txt.upper() == 'EURO':
        moeda = dinheiro['Euro']
    elif txt.upper() == 'REAL':
        moeda = dinheiro['Real']
    elif txt.upper() == 'DOLAR':
        moeda = dinheiro['Dolar']
    else:
        moeda = dinheiro['Libra']

    return moeda
