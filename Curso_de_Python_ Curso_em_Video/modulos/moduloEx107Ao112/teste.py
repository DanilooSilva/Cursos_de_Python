from moduloEx107Ao112.utilidades import moedas, dados

preco = dados.leiaDinheiro('Digite um preço: R$')
moedas.resumo(preco, 80, 35)
