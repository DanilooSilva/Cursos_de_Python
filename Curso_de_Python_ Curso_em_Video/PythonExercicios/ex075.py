numeros = (
            int(input('Digite um número: ')), int(input('Digite outro número: ')),
            int(input('Digite mai um número: ')), int(input('Digite o último número: '))
          )
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição' if 3 in numeros else 'O valor 3 não foi digitado nenhuma vez.')
print('Os valores pares digitados foram ', end='')
for par in numeros:
    if par % 2 == 0:
        print(f'{par}', end=' ')
