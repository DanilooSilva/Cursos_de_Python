print('Cadastre Uma Pessoa')
totMa18 = totH = totMMe20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        totMa18 += 1
    if sexo in 'M':
        totH += 1
    if sexo in 'F' and idade < 20:
        totMMe20 += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totMa18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totMMe20} mulheres com menos de 20 anos')