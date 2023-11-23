num_0_20 = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
            'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
            )
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        break
    else:
        print('Tente novamente!! ', end='')

print(f'você digitou o numero: {num_0_20[num]}')