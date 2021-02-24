from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

nova_lista_2 = [x for x in lista if x > 5]
print(list(nova_lista_2))


lista_produto = filter(lambda p: p['preco'] > 50, produtos)
print(list(lista_produto))



