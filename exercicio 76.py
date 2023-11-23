produtos = (
    'lapis',1.75,
    'borracha',2.00,
    'caderno',15.90,
    'estojo',25.00,
    'transferidor',4.20,
    'compasso',9.99,
    'mochila',120.32,
    'canetas',22.30,
    'livro',34.90
)

print('-' *42)
print(f"{'LISTAGEM DE PREÇOS':^42}")
print('-' *42)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}R${produtos[i+1]:>10}')

print('-' *42)