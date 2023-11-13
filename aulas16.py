num_0_20 = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
            'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
            )

num = int(input('Digite um número entre 0 e 20: '))


for pos, i in enumerate(num_0_20):
    if num == pos: 
        print(f'Você digitou o número {num_0_20[pos]}')
        break
    elif num != pos: 
        print('Tente novamente.')
        break
