largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura

tinta = area / 2
print('A área da parede é de {}'.format(area))
print('Será necessário para pintar {} litros de tinta'.format(tinta))
