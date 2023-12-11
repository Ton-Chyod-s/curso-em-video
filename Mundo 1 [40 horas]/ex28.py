from random import randint
from time import sleep

numero = randint(0,5)
print('Ja pensei, tente adivinhar o número que eu sei!')
num = int(input('Em que numero pensei de 0 a 5: '))
print(f'\033[32mPROCESSANDO...\033[m')
sleep(1)
if num == numero:
    print(f'\033[33mVocê venceu!!\nO número que eu escolhi foi {numero}\033[m')
else:
    print(f'\033[31mVocê perdeu!!\nO número que eu escolhi foi {numero}\033[m')