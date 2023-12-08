from random import shuffle

aluno = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno,aluno2,aluno3,aluno4]
shuffle(lista)
print(f'A ordem de apresentação é\n{lista}')
