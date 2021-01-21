import random

aluno1 = input('Digite o nome do 1° Aluno ')
aluno2 = input('Digite o nome do 2° Aluno ')
aluno3 = input('Digite o nome do 3° Aluno ')
aluno4 = input('Digite o nome do 4º Aluno ')

print('O aluno sorteado para apagar o quadro foi {}'.format(random.choice([aluno1,aluno2,aluno3, aluno4])))
