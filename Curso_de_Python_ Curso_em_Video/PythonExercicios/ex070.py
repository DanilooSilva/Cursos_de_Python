print('-*-' * 30)
print('Loja Super Baratão')
print('-*-' * 30)
totalCompra = contMaisDeMil = precoMaisBarato = cont = 0
produtoMaisBarato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    totalCompra += preco
    cont += 1
    if cont == 1:
        precoMaisBarato = preco
        produtoMaisBarato = produto
    if precoMaisBarato > preco:
        precoMaisBarato = preco
        produtoMaisBarato = produto
    if preco > 1000:
        contMaisDeMil += 1
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break
print('{:-^40}'.format(' Fim do Programa '))
print(f'O total da compra foi R$ {totalCompra:.2f}')
print(f'Temos {contMaisDeMil} produto custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produtoMaisBarato} que custa R$ {precoMaisBarato:.2f}')