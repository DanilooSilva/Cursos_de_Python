print('=' * 40, 'Informe 3 reta para verificar se forma um triângulo ' + '=' * 40)
r1 = float(input('Informe a 1° reta: '))
r2 = float(input('Informe a 2ª reta: '))
r3 = float(input('Informe a 3ª reta: '))

if r2 - r3 < r1 and r2 + r3 > r1 and r1 - r3 < r2 and r1 + r3 > r2 and r1 - r2 < r3 and r1 + r2 > r3:
    print('As retas informada forma um triângulo!')
else:
    print('As retas não forma um triângulo!')