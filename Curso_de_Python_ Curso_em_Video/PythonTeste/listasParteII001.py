'''teste = list()
teste.append('Danilo')
teste.append(26)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['Jão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera[2][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''

galera = list()
dados = list()
totalmaior = totamenor = 0
for c in range(0,3):
    dados.append(str(input('Nome: ')).strip())
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totamenor += 1
print(f'Temos {totalmaior} maiores e {totamenor} menor de idade')