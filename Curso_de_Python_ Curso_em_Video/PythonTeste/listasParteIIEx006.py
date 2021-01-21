alunos = list()
nomes = list()
notas = list()
media = somanota = n1 = n2 = cont = 0
while True:
    nomes.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nomes.append(notas[:])
    alunos.append(nomes[:])
    notas.clear()
    nomes.clear()
    continuar = str(input('Continuar ? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Continuar ? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=-' * 30)
print(f'{"N°":<4} {"Nome":<30} {"Média":<15}')
print('-' * 60)
for a in alunos:
    for n in range(0, len(a[1])):
        media = (a[1][0] + a[1][1]) / 2
    print(f'{cont:<4} {a[0]:<30} {media:>5.2f}')
    cont += 1
print('-' * 60)
while True:
    mostrar = int(input('Mostrar Notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    if mostrar in range(0, len(alunos)):
        print(f'Notas de {alunos[mostrar][0]} {alunos[mostrar][1]}')
    else:
        print('Opção Invalida')
    print('-' * 60)
print('Finalizando...')
print('Volte sempre!')
