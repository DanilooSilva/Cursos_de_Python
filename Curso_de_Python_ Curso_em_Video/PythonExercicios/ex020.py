# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample, shuffle

a1 = input('1° Aluno: ')
a2 = input('2º aluno: ')
a3 = input('3º aluno: ')
a4 = input('4º aluno: ')

sor = sample([a1,a2,a3,a4], k=4)
lista = [a1, a2, a3, a4]
shuffle(lista)


print('A order de apresentação do trabalho {}'.format(sor))
print('A order de apresentação será ')
print(lista)
