print('-=-' * 30)
print('Sequância de Fibonacci')
print('-=-' * 30)
termo = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
cont = 3
while cont <= termo:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    cont += 1
print('fim')