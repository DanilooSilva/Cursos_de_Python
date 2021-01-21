print('-=-' * 30)
print('Analisador de Triângulos ')
print('-=-' * 30)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if b - c < a and b + c > a and a - c < b and a + c > b and a - b < c and a + b > c:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if a == b and b == c:
        print('É um triângulo Equilátero!')
    elif a != b and b == c or a == b and b != c:
        print('É um triângulo Isósceles!')
    else:
        print('É um triângulo Escaleno!')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo')
