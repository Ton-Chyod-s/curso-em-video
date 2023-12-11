cidade = str(input('Em que cidade você nasceu? ')).strip().upper()
cidade = cidade.split()
if cidade[0] == 'SANTO':
    print('True')
else:
    print('False')