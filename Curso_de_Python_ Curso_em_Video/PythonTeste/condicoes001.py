cores = {'limpa':'\033[m',
          'vermelho':'\033[31m',
           'azul': '\33[34m',
           'verde': '\33[32m'}


nome = str(input('{}Qual é seu nome?{} '.format(cores['azul'], cores['limpa'])))

if nome == 'Danilo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))