from random import randint
from time import sleep

print('-=' * 24)
numero_pensou = randint(0,5)
print('Ja pensei, tente adivinhar o número que eu sei!')
num = int(input('Em que numero pensei de 0 a 5: '))
print('-=' * 24)
print(f'\033[32mPROCESSANDO...\033[m')
sleep(.8)
if num == numero_pensou:
    print(f'\033[33mPARABÉNS!! Você venceu.. \033[m')
else:
    print(f'\033[31mQUE PENA!! Você perdeu..\nEu pensei no {numero_pensou} e não no {num}\033[m')
