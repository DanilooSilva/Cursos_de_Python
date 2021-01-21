valorProduto = float(input('Digite o valor do produto: '))
formaPg = int(input('Escolha a forma de pagamento 1 - Avista, 2 - Cédito avista, 3 - Crédito até 2x, 4 Crédito acima de 3x: '))

if formaPg == 1:
    valorProduto = valorProduto - (valorProduto * 10 / 100)
    print('Você ganhou 10% de desconto! Agora o preço do produto é R$ {:.2f}'.format(valorProduto))
elif formaPg == 2:
    valorProduto = valorProduto - (valorProduto * 5 / 100)
    print('Você ganhou 5% de desconto! Agora o preço do Produto é: R$ {:.2f}'.format(valorProduto))
elif formaPg == 3:
    print('O produto sem juros e sem desconto R$ {:.2f}'.format(valorProduto))
elif formaPg == 4:
    valorProduto = valorProduto + (valorProduto * 20 / 100)
    print('Com o parcelamento acima de 2x o valor do produto tem um acrescimo de 20% e passa ser: R$ {:.2f}'.format(valorProduto))
else:
    print('Opção invalida.')