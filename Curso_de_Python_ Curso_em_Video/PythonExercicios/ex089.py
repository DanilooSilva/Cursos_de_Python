alunos = []
nome = nota1 = nota2 = media = 0
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    alunos.append([nome, [nota1, nota2]])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=' * 40)
print(f'{"N°":<3} {"NOME":<10} {"MÈDIA":>20}')
print('-' * 40)
for i, a in enumerate(alunos) :
    for n in range(0, len(a[1])):
        media = (a[1][0] + a[1][1]) / 2
    print(f'{i:<3} {a[0]:<10} {media:>20.1f}')
print('-' * 40)
while True:
    aluno = int(input('Mostrar as nostas de qual aluno? (999 para sair): '))
    if aluno >= 999:
        break
    if aluno in range(0, len(alunos)):
        print(f'Nota de {alunos[aluno][0]} são {alunos[aluno][1]}')
print('Finalizando...')
print(f'<<< Volte Sempre >>>')