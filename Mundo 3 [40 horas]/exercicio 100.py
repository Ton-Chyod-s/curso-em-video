from random import randint
from time import sleep
def sorteia():
    num = [randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)] 
    return num


def somaPar():
    num_par = 0
    lista = sorteia().copy()
    print(f'Sorteando os {len(lista)} valores da lista', end=' ')
    for i in lista:
        sleep(.3)
        print(i, end = ' ')
    print('PRONTO!')
    for i in lista:
        if i % 2 == 0:
             num_par += i
    print(f'Somando os valores pare de {lista}, temos',end=' ')
    return num_par
   

print(somaPar())
