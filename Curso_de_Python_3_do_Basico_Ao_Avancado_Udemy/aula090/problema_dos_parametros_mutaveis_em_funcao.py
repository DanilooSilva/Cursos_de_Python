def lista_de_clientes(clientes_interavel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_interavel)
    return lista


lista_clientes_1 = ['Danilo']
clientes1 = lista_de_clientes(
    ['Maria', 'Nazaré', 'Allanys'],
    lista_clientes_1
    )

clientes2 = lista_de_clientes(['Scarllet', 'Ohara', 'Mel'])
clientes3 = lista_de_clientes(['Jose'])


print(clientes1)
print(clientes2)
print(clientes3)