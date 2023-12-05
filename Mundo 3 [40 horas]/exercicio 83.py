conta = str(input('Digite uma expressão: '))
pilha = []

for i in conta:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) ==0:
    print('sua expressão esta correta')
else:
    print('sua expressão esta incorreta')
