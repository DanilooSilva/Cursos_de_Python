#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na
# tela o valor do seno, cosseno e tangente desse ângulo.

import math
an = float(input('Digite o ângulo que você deseja: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))

print('O ângulo de {} tem o SENO de {:.2f}'.format(an, se))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, co))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(an, ta))
