#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

a = float(input('1° seguimento: '))
b = float(input('2° seguimento: '))
c = float(input('3° seguimento: '))

if a - b < c and a + b > c and b - c < a and b + c > a and a - c < b and a + c > b:
    if a == b and b == c:
        print('Os seguimentos acima podem formar um triângulo Equilátero')
    elif a != b and b == c or a == b and b != c or a == c and c != b:
        print('Os seguimentos acima podem formar um triângulo Isósceles')
    else:
        print('Os seguimentos acima podem formar um triângulo Escaleno')
else:
    print('Os seguimentos acima não formam um triângulo!')