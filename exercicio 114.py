from urllib.request import urlopen
from urllib.error import URLError

import urllib
import urllib.request

url = 'http://pudim.com.br/'

try:
    with urlopen(url) as resposta:
        if resposta.getcode() == 200:
            print('Consegui acessar o site Pudim com sucesso!')
            """site = urllib.request.urlopen(url)
            print(site.read())"""
except URLError:
    print('O site Pudim não esta acessivel no momento.')