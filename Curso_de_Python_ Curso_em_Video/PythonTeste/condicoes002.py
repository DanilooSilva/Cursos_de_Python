n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('A sua média foi {:.1f}'.format(m))

print('Parabéns!' if m >= 6 else 'Estude Mais!')
if m >= 6:
    print('Sua média foi boa')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')