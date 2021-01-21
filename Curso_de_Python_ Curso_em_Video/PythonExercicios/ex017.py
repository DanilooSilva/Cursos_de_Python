#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot
oposto = float(input('Comprimento o cateto oposto '))
adjacente = float(input('Comprimento o cateto adjacente '))
hipotenusa = hypot(oposto, adjacente)         #(oposto ** 2 + adjacente ** 2) ** (1/2)
print('A hipotenusa é {:.2f}'.format(hipotenusa))
