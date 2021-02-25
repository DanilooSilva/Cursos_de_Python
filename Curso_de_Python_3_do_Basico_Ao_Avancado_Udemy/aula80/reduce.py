from dados import pessoas, produtos, lista
from functools import reduce


soma_lista = reduce(lambda ac, i: i + ac, lista, 0)

print(soma_lista)

soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(round(soma_preco, 2))

