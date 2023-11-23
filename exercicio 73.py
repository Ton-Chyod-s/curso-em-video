times = (
    'palmeiras', 'botafogo', 'grêmio', 'bragantino', 'atlético-MG', 'flamengo', 'atlético-PR',
    'fluminese', 'cuiabá', 'são paulo', 'corinthians', 'fortaleza', 'internacional', 'santos',
    'vasco da gama', 'cruzeiro', 'bahia', 'goiás', 'coritiba', 'américa-MG'
)

#a) Os 5 primeiros times.
print(times[0:5])
#b) Os últimos 4 colocados.
print(times[-4:])
#c) Times em ordem alfabética.
print(sorted(times))
#d) Em que posição está o time da Chapecoense.

for i in times:
    posicao = 0
    if i == 'chapecoense':
        posicao += 1
    else:
        print('não encontrada na tabela')
        break