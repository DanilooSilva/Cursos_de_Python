cont = 0
mediaIdade = 0
maiorIdade = 0
nomeMaisVelho = ''
for c in range(0, 4):
    nome = str(input('nome:  ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    if sexo == 'F':
        cont += 1
    mediaIdade += idade
    if c == 0 and sexo in 'M':
        maiorIdade = idade
        nomeMaisVelho = nome
    if sexo in 'M' and idade > maiorIdade:
        maiorIdade = idade
        nomeMaisVelho = nome

mediaIdade = mediaIdade / 4
print('A média de idade é {}'.format(mediaIdade))
print('Neste grupo tem {} mulheres'.format(cont))
print('O {} é o homen mais velho do grupo.'.format(nomeMaisVelho))
