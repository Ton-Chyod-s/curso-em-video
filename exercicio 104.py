def leiaInt(txt):
    print('-=' * 15)
    while True:
        num = str(input(txt))
        if num.isnumeric():
            return num
        else:
            print(f"\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        

n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')