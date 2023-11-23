times = (
    'palmeiras', 'botafogo', 'grêmio', 'bragantino', 'atlético-MG', 'flamengo', 'atlético-PR',
    'fluminese', 'cuiabá', 'são paulo', 'corinthians', 'fortaleza', 'internacional', 'santos',
    'vasco da gama', 'cruzeiro', 'bahia', 'goiás', 'coritiba', 'américa-MG'
)

#a) Os 5 primeiros times.
print(f'5 primeiros times: {times[0:5]}')
#b) Os últimos 4 colocados.
print(f'Últimos 4 colocados: {times[-4:]}')
#c) Times em ordem alfabética.
print(f'Ordem alfabética: {sorted(times)}')
#d) Em que posição está o time da Chapecoense.
for i in times:
    if i == 'chapecoense':
        print(f'Posição: {times.index("chapecoense")}')
    