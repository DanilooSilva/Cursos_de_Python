print('-=-' * 30)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
cont = 1
soma = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo += razao
        cont += 1
    print('Pause')
    mais = int(input('Quantos termos você quer mostra mais ? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
