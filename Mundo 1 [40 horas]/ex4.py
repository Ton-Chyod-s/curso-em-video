txt = input('Digeite algo: ')

print(f'O tipo primitivo desse valor é: {type(txt)}')  
print(f'Só tem espaços? {txt.isspace()}')
print(f'É um numero? {txt.isnumeric()}')
print(f'É alfabetico? {txt.isalpha()}')
print(f'É alfanumerico? {txt.isalnum()}')
print(f'Está em maiusculas? {txt.isupper()}')
print(f'Está em minuscula? {txt.islower()}')
print(f'Está capitalizada? {txt.istitle()}')