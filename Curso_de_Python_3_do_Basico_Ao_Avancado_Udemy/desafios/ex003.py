carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produdo 2', 20))
carrinho.append(('Produdo 3', 50))

valor_total = sum([(y) for x, y in carrinho])

print(valor_total)