prodPreco = (
                ('Lapis', 1.57),                ('Borrahca', 2.00),
                ('Caderno', 15.90),             ('Estojo', 25.00),
                ('Transferidor', 4.20),         ('Compasso', 9.99),
                ('Mochila', 120.32),            ('Canetas', 22.30),
                ('Livros', 34.90)
            )
print('-' * 50)
print('{:^50}'.format('Listagem de Preços'))
print('-' * 50)
for prod, preco in prodPreco:
    print(f'{prod:.<30} R$ {preco:>7.2f}')
print('-' * 50)