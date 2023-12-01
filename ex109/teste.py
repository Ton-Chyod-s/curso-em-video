import moeda

num= float(input('Digite um preço: R$'))
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(num,10))}')
print(f'Diminuindo 30%, temos {moeda.moeda(moeda.diminuir(num,30))}')
print(f'A dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')