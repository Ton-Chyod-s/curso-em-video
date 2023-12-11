velocidade = float(input('Qual a veloicidade do carro? '))
if velocidade > 80:
    print(f'\033[031mMULTADO!! Você excedeu o limite de 80Km/h\nVocê deve pagar uma multa de\033[m \033[33mR${(velocidade - 80) * 7}!\033[m')
print(f'\033[033mTenha um bom dia! Dirija com segurança!\033[m')