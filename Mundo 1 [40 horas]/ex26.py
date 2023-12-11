frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra "a" aparece: {frase.count("A")} vezes')
print(f'A primeira posição é: {frase.index("A")+1}')
print(f'A ultima posição é: {frase.rindex("A")+1}')