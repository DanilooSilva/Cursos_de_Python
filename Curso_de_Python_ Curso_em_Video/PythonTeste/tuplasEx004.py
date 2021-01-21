numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número:')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
cont = 0
indexNumero3 = 0
numerosPares = 0
for n in numeros:
    if n == 9:
        cont += 1
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {cont} vezes')
for n3 in range(0, len(numeros)):
    if numeros[n3] == 3:
        indexNumero3 = numeros.index(3)  + 1
if indexNumero3 > 0:
    print(f'O valor 3 apareceu na {indexNumero3}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for pares in numeros:
    if pares % 2 == 0:
        numerosPares = pares
if numerosPares != 0:
    print('Os valores pares digitados foram ', end='')
    for par in numeros:
        if par % 2 == 0:
            print(par, end=' ')
else:
    print('Não foi digitado nenhum número par')