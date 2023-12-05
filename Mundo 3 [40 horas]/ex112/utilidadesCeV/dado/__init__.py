def leiaDinheiro():
    while True:
        num = str(input("Digite o preço: R$")).replace(",",".")
        numero = num.replace(".", "", 1).isdigit()
        if numero:
            num = float(num)
            return num
        print(f'\033[0;31mERRO: {num.strip()} é um preço inválido!\033[m')

if __name__ == '__main__':
    leiaDinheiro()