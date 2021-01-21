produtosPreco = (('Lapis', 1.75),        ('Borracha', 2.00),              ('Caderno', 15.90),
                 ('Estojo', 25.00),      ('Transferidor', 4.20),          ('Compasso', 9.99),
                 ('Mochila', 120.32),    ('Canetas', 22.30),              ('Livro', 34.90))

print('-' * 40)
print('{:^40}'.format(' Listagem de produtos '))
print('-' * 40)
for produto, valor in sorted(produtosPreco):
    print(f'{produto}', '{:^1}'.format('.') * 20, f'R${valor:.2f}')
print('-' * 40)