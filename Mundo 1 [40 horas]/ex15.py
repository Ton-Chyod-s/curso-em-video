km = float(input('Digite os Km percorridos: '))
dia = int(input('Digite os dias que ele foi alugado: '))
k = km * 0.15
d = dia * 60
print(f'O total a pagar é de R${k + d:.2f}')