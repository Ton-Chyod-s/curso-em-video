from datetime import date
from calendar import isleap

data = date.today()
ano =  data.year
anoU = int(input('Que ano quer analisar? '))
bissexto = isleap(anoU)
if bissexto and anoU != 0:
    print(f'O ano {anoU} é um ano bissexto!')
else:
    if anoU == 0:
        anoU = ano
    print(f'O ano {anoU} Nem é bissexto!')