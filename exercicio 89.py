sala = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = nota1 + nota2 / 2
    sala.append([nome,[nota1,nota2],media])
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-=' * 15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 15)
for num, i in enumerate(sala):
    print(f'{num:<4}{i[0]:<10}{i[2]:>8.1f}')

while True:
    notas = int(input('Mostrar notas de qual aluno? [999 interrompe]'))
    if notas == 999:
        break
    if notas <= len(sala) -1:
        print(f'Notas de {sala[notas][0]} são de {sala[notas][1]}' )
print('<< Volte sempre >>')