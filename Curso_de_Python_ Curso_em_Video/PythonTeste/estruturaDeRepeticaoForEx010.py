pesoLista = []
for c in range(0, 5):
    peso = float(input('Digite o peso: '))
    pesoLista.append(peso)

print('O menor peso é {}.'.format(min(pesoLista)))
print('O maior peso é {}.'.format(max(pesoLista)))