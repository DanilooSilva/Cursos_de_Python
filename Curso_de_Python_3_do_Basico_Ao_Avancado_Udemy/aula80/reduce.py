from dados import pessoas, produtos, lista
from functools import reduce
from Curso_de_Python_3_do_Basico_Ao_Avancado-Udemy.aula78 import *


soma_lista = reduce(lambda ac, i: i + ac, lista, 0)

print(soma_lista)

soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(round(soma_preco, 2))

