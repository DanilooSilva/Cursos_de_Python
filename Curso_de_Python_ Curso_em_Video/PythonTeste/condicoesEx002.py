velo = float(input('Qual é a velocidade do carro: '))

if velo > 80:
    m = (velo - 80) * 7
    print('Carro multado em R$ {:.2f}'.format(m))
