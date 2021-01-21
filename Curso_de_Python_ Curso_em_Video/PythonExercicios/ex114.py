import urllib.request

try:
    site = urllib.request.urlopen('https://google.com.br')
except urllib.error.URLError:
    print('Erro: site não acessível:')
else:
    print('Site acessível')