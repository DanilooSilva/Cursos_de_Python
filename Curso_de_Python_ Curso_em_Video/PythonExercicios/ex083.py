ex = str(input('Digite a expressão: ')).strip()
contabre = contfecha =  cont =0
for letra in ex:
    if letra in '(':
        contabre += 1
        cont += 1
    if letra in ')':
        contfecha += 1
        cont += 1
if cont % 2 == 0 and contabre == contfecha :
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')