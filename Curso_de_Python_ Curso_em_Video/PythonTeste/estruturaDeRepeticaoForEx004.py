tabuada = int(input('Qual tabuada que deseja saber: '))
result = 0

for c in range(0, 11):
    result = tabuada * c
    print('{} x {:2} = {}'.format(tabuada, c, result))
