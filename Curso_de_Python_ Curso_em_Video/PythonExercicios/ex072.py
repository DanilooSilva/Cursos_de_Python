numeroExtenso = ('Zero',                            'Um',                               'Dois',
                 'Três',                            'Quatro',                           'Cinco',
                 'Seis',
                 'Sete',                            'Oito',                             'Nove',
                 'Dez',                             'Onze',                             'Doze',
                 'Treze',                           'Quatorze',                         'Quinze',
                 'Dezesseis',                       'Dezessete',                        'Dezoito',
                 'Dezenove',                        'Vinte')
numeroUsuario = int(input('Digite um número entre 0 e 20: '))
while numeroUsuario < 0 or numeroUsuario > 20:
    numeroUsuario = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Voce digitou o número {numeroExtenso[numeroUsuario]}')