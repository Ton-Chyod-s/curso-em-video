def aumentar(num,aumentar):
    porc = aumentar
    aumen = num * porc/100
    return f'Aumentando R${porc}%, temos R${float(num + aumen)}'


def diminuir(num,diminuir):
    porc = diminuir
    dimi = num * porc/100
    return f'Diminuindo R${porc}%, temos R${float(num - dimi)}'


def dobro(num):
    return f'O dobro de R${num} é R${float(num * 2)}'


def metade(num):
    return f'A metade de R${num} é R${float(num / 2)}'

