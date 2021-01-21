#! python3
from datetime import datetime
from desafios.loja import Cliente, Vendedor, Compra

def main():
    cliente = Cliente('Danilo Gomes', 26)
    vendedor = Vendedor('Pedro', 36, 5758.5)
    compra1 = Compra(vendedor, datetime.now(), 512.99)
    compra2 = Compra(vendedor, datetime(2018, 6, 4), 256.97)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)

    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adulto() else '')
    print(f'Vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    qtde_compras = len(cliente.compras)
    print(f'Total: {valor_total} em {qtde_compras} compras')
    print(f'Últma compra {cliente.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()

