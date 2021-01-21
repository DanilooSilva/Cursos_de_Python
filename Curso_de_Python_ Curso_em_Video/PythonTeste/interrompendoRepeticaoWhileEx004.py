maior18 = qntH = mMenor20 = 0
while True:
    print('-' * 30)
    print('Cadstre uma Pessoa')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    print('-' * 30)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo in 'M':
        qntH += 1
    if sexo in 'F' and idade < 21:
        mMenor20 += 1
    if continuar == 'N':
        break
print('=' * 7, ' Fim do Programa ', '=' * 7)
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {qntH} homens cadastrados')
print(f'E temos {mMenor20} mulher com menos de 20 anos')