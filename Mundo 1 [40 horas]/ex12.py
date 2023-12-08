preco = float(input('Digite o valor de um produto: R$'))
desconto = preco * 0.05
print(f'O produto custava R${preco}, na promoção com desconto de 5% por R${preco - desconto:.2f}')