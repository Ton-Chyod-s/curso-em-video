num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))

lista_tup = (num1,num2,num3,num4)

print(f'Você digitou os valores {lista_tup}')

#A) Quantas vezes apareceu o valor 9.
apareceu = 0
for i in lista_tup:
    if 9 in lista_tup:
        apareceu += 1

if apareceu == 0:
    print('Não foi econtrado o número 9')
else:
    print(f'O valor 9 apareceu: {apareceu} vezes')
    
#B) Em que posição foi digitado o primeiro valor 3.
if 3 in lista_tup:
    print(f'O valor 3 apareceu na {lista_tup.index(3)+1}º posição')
else:
    print('Não foi econtrado o número 3')

#C) Quais foram os números pares.
print(f'Os valores pares foram ', end = '')
for i in lista_tup:
    if i % 2 == 0:
        print(i, end = ' ')

    