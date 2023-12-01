def voto(ano_nascimento):
    from datetime import date
    data_atual = date.today()
    if data_atual.year - ano_nascimento == 1 or data_atual.year - ano_nascimento < 18:
        res = 'VOTO NEGADO'
    elif data_atual.year - ano_nascimento >= 18 and data_atual.year - ano_nascimento < 65:
        res =  'VOTO OBRIGATÓRIO'
    else:
        res = 'VOTO OPCIONAL'
    return F'Com {data_atual.year - ano_nascimento} anos: {res}'

print('-=' * 20)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))