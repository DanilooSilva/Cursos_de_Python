#Exercício Python 035: Desenvolva um programa que leia o
# comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 30)
print('Analisador de Triângulos ')
print('-=-' * 30)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if b - c < a and b + c > a and a - c < b and a + c > b and a - b < c and a + b > c:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo')
