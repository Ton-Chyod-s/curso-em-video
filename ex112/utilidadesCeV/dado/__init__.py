def leiaDinheiro():
    while True:
        num = str(input("Digite um valor: "))
        if num.isnumeric():
            num = float(num.replace("," , "."))
            print(num)
            return num
        print(f'ERRO: {num} é um preço inválido!')

if __name__ == '__main__':
    leiaDinheiro()