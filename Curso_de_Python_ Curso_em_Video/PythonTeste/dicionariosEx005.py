dados = {}
pessoas = []
mulheres = []
pessoaIdade = []
contP = mediaI = 0
while True:
    nome = str(input('Nome: ')).strip().title()
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    idade = int(input('Idade: '))
    contP += 1
    dados['nome'] = nome
    dados['sexo'] = sexo
    dados['idade'] = idade
    pessoas.append(dados.copy())
    if sexo in 'F':
        mulheres.append(dados.copy())
    dados.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
for i, p in enumerate(pessoas):
    mediaI += p['idade']
mediaI /= contP
for p in pessoas:
    if p['idade'] > mediaI:
        pessoaIdade.append(p.copy())
print('-=' * 30)
print(f' - O grupo tem {contP} pessoas.')
print(f' - A média de idade é de {mediaI:.2f}')
print(' - A mulheres Cadastradas foram: ', end='')
for mu in range(0, len(mulheres)):
    print(f'{mulheres[mu]["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média:')
print()
for pI in pessoaIdade:
    print(f'nome = {pI["nome"]}; sexo = {pI["sexo"]}; idade = {pI["idade"]}')
print('<<< Encerrando >>')
