from .map import produtos, pessoas, lista

#nova_lista = map(lambda x: x * 2, lista)

# nova_lista = [n * 2 for n in lista]

# print(lista)
# print(list(nova_lista))

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)
# precos = map(lambda p: p['preco'], produtos)

for produto in novos_produtos:
    print(produto['preco'])


nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)
