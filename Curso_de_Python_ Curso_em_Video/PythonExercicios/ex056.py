#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
maisVelho = 0
nomeMaisvelho = ''
contMulheres = 0
for c in range(1, 5):
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade / 4
    if sexo == 'F' and idade < 18:
        contMulheres +=1
    if c == 1 and sexo == 'M':
        maisVelho = idade
        nomeMaisvelho = nome
    elif sexo == 'M':
        if idade > maisVelho:
            maisVelho = idade
            nomeMaisvelho = nome

print('A média de idade é {:.1f} anos'.format(media))
print('O home mais velho tem {} anos e se chama {}'.format(maisVelho, nomeMaisvelho))
print('Ao todo são {} mulheres com menos de 18 anos'.format(contMulheres))