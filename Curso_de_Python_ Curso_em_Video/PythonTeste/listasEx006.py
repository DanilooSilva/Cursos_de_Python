exprecao = str(input('Digite a expressão: ')).strip()
lista = list()
cont = 0
for n in exprecao:
    lista.append(n)
for ex in lista:
    if '(' in ex:
        cont += 1
    if ')' in ex:
        cont += 1
if cont % 2 == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada!')
