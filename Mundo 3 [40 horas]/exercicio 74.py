from random import randint


lista_num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print('-=' * 15)
print(f'A lista é: {lista_num}'.replace('(','').replace(')',''))
print('-=' * 15)
print(f'O maior é: {max(lista_num)}')
print('-=' * 15)
print(f'O menor é: {min(lista_num)}')
print('-=' * 15)