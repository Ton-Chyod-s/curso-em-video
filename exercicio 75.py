num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))

lista_tup = (num1,num2,num3,num4)

#A) Quantas vezes apareceu o valor 9.
apareceu = 0
for i in lista_tup:
    if i == 9:
        apareceu += 1

if apareceu == 0:
    print('Não foi econtrado o número 9')
else:
    print(f'O numero 9 apareceu: {apareceu}')
    
#B) Em que posição foi digitado o primeiro valor 3.
try:
    print(f'o numero 3 foi encontrado na posicão: {lista_tup.index(3)}')
except:
    print('Não foi econtrado o número 3')

#C) Quais foram os números pares.
for i in lista_tup:
    if i % 2 == 0:
        print(f'Número par: {i}')

    