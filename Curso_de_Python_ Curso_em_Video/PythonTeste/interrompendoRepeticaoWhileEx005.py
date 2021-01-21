totalGasto = maior1000 = cont = precoBarato = 0
maisbarato = ''
print('=' * 30)
print('Loja Super Baratão')
print('=' * 30)
while True:
    nomeProduto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: '))
    continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    totalGasto += preco
    cont += 1
    if preco > 1000:
        maior1000 += 1
    if cont == 1:
        precoBarato = preco
        maisbarato = nomeProduto.title()
    if precoBarato > preco:
        precoBarato = preco
        maisbarato = nomeProduto.title()
    if continuar == 'n':
        break
print('_' * 10, ' Fim do Programa', '_' * 10)
print(f'O total da compra foi R$ {totalGasto:.2f}')
print(f'Temos {maior1000} produtos custando mais que R$ 1000.00')
print(f'O produto mais barato foi {maisbarato} que custa R$ {precoBarato:.2f}')