from math import hypot

c_a = float(input('Digite o valor do cateto adjacente: '))
c_o = float(input('Digite o valor do cateto oposto: '))

print(f'A hipotenusa do triagulo é {hypot(c_a,c_o):.2f}')