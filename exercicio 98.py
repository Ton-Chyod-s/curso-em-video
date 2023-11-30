from time import sleep
def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if str(passo)[0] == '-':
        passo = int(passo[1])
    elif passo == 0:
        passo = 1
    if inicio > fim:
        lista = []
        for i in range(fim, inicio+1, passo):
            lista.append(i)
        lista.reverse()
        for i in lista:
            print(i,end=' ')
            sleep(.5)
    else:
        for i in range(inicio, fim+1, passo):
            print(i,end=' ')
            sleep(.5)
    print('FIM !!')

    
contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez!!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = str(input('Passo: '))
contador(inicio,fim,passo)