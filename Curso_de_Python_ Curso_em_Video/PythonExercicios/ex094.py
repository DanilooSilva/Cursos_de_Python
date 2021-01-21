pessoas = []
pessoa = {}
mediaIdade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Erro! Por favo, digite apenas M ou F ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Erro! Responda apenas S ou N: ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=' * 30)
print(f'A)  Total de pessoas Cadastrads {len(pessoas)}')
for i in pessoas:
    mediaIdade = (mediaIdade + i['idade'])
mediaIdade /= len(pessoas)
print(f'B)  A média de idade é de {mediaIdade:.2f} anos.')
print('C)  As mulheres cadastradas foram ', end='')
for m in pessoas:
    if m['sexo'] in 'F':
        print(f'{m["nome"]} ', end='')
print()
print('D)  Lista das pessoas que estão acima da média: ')
for acm in pessoas:
    if acm['idade'] >= mediaIdade:
        print('    ', end='')
        for k, v in acm.items():
            print(f'{k} = {v:}; ', end='')
        print()
print('<< ENCERRANDO >>')
