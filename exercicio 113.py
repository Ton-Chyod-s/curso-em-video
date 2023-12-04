def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except ValueError:
            print(f'\033[0;31mERRO: por favor, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print(f'\033[0;31mUsuário prefiriu não digitar o número\033[m')
        else:
            return num


def leiaFloat(txt):
    while True:
        try:
            num = float(input(txt).replace(",","."))
        except ValueError:
            print(f'\033[0;31mERRO: por favor, digite um número real válido\033[m')
        except KeyboardInterrupt:
            print(f'\033[0;31mUsuário prefiriu não digitar o número\033[m')
        else:
            return num
        

print('-=' * 15)
n = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {n2}')