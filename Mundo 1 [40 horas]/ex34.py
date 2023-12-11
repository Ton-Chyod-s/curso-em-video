salario = float(input('Digite seu salário: R$'))
if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15
print(f'Seu salario era R${salario} agora com um aumento de 10% passou a ser R${salario + aumento}')
