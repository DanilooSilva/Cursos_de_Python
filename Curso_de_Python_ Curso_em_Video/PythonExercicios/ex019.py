# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido

import random
a1 = input('1° Aluno: ')
a2 = input('2º aluno: ')
a3 = input('3º aluno: ')
a4 = input('4º aluno: ')

sor = random.choice([a1,a2,a3,a4])

print('O aluno sorteado foi {}'.format(sor))