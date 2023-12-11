print('-=' * 23)
print('\033[1;32mAnalisador de Triângulo\033[m')
print('-=' * 23)
a = float(input('Digite primeiro segmento: '))
b = float(input('Digite segundo segmento: '))
c = float(input('Digite terceiro segmento: '))

cond1 = (b - c) < a < b + c
cond2 = (a - c) < b < a + c
cond3 = (a - b) < c < a + b
if cond1 and cond2 and cond3:
    res = '\033[1;32mPODEM FORMAR\033[m'
else:
    res = '\033[1;31mNÃO PODEM FORMAR\033[m'
print(f'Os segmentos acima {res} \033[33mTriângulo!\033[m')