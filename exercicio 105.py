def notas(*args, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param args:uma ou mais notas dos alunos (aceita várisa)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com várias informações sobre a situação da turma. 
    """
    lista_alunos = args
    dicionario_alunos = {}
    calculo = {}
    for num, valor in enumerate(lista_alunos):
        dicionario_alunos[f'aluno {num+1}'] = valor
    calculo['total'] = len(dicionario_alunos)
    calculo['maior'] = max(dicionario_alunos.values())
    calculo['menor'] = min(dicionario_alunos.values())
    calculo['média'] = sum(dicionario_alunos.values()) / len(dicionario_alunos)
    if sit:
        if calculo['média'] >= 7:
            res = 'BOA'  
        elif calculo['média'] >= 5:
            res = 'RAZOÁVEL'  
        else:
            res = 'RUIM'
        calculo['situação'] = res
    return calculo



print(notas(7.5,3.5,9.5,sit=True))