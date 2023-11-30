def maior(*args):
    print('-=' * 20)
    print('Analisando os valores passado...')
    maior = 0
    for i in args:
        if i > maior:
            maior = i
    for i in args:
        print(i, end=' ')
    print(f'Foram informados {len(args)} ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()