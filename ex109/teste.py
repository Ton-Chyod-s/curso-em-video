import moeda

num= float(input('Digite um preço: R$'))
print(f'Aumentando 10%, temos {moeda.aumentar(num,10,True)}')
print(f'Diminuindo 30%, temos {moeda.diminuir(num,30,True)}')
print(f'A dobro de {moeda.moeda(num)} é {moeda.dobro(num,True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num,True)}')