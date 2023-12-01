def fatorial(num, show=False):
    """-> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número num."""
    fat = 1
    calculo = []
    for i in range(1, num+1):
        fat *= i
        calculo.append(i)
    if show:
        calculo.reverse()
        cont = 0
        for valor in calculo:
            print(valor, end= ' ')
            if len(calculo) - cont != 1:
                print('X', end = ' ')
                cont += 1
        print('=', end=' ')
        return fat
    else:
        return fat
    

print('-=' * 20)
print(fatorial(5,True))