distancia = float(input('Digite a distancia da viagem km/h: '))

if distancia <= 200:
    print(f'O preço da viagem será de R${distancia * .50}')
else:
    print(f'O preço da viagem será de R${distancia * .45}')