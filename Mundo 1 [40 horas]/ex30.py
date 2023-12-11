num = int(input('Digite um número: '))
if num % 2 != 1:
    print(f'O {num} é um numero \033[32mPAR!\033[m')
else:
    print(f'O {num} é um numero \033[34mIMPAR!\033[m')