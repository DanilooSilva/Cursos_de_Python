print('Digite 3 números ')
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3° número: '))

if n1 > n2 and n1 > n3:
    print('O maior número digitado foi {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print(' O maior número digitado foi {}'.format(n2))
else:
    print('O maior número digitado foi {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor número digitado foi {}'. format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor número digitado foi {}'.format(n2))
else:
    print('O menor número digitado foi {}'.format(n3))