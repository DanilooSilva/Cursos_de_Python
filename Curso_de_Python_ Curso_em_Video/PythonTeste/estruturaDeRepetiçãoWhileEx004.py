mult = 1
valor = int(input('Digite um valor: '))
novovalor = valor
while novovalor > 1:
    mult *= novovalor
    novovalor -= 1
print('O Fatorial de {} é {}'.format(valor, mult))