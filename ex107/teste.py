import moeda

num= float(input('Digite um preço: R$'))
print(f'Aumentando 10%, temos R${moeda.aumentar(num,10)}')
print(f'Diminuindo 30%, temos R${moeda.diminuir(num,30)}')
print(f'A dobro de R${num} é R${moeda.dobro(num)}')
print(f'A metade de R${num} é R${moeda.metade(num)}')