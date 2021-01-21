from datetime import  datetime


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade} anos'

    def is_Adulto(self):
        return True if self.idade > 18 else False


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registra_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        return self.compras[-1].data

    def total_compras(self):
        return sum(self.compras[i].valor for i in range(len(self.compras)))


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor


def main():
    danilo = Cliente('Danilo Gomes', 28)
    maria = Vendedor('Maria', 28, 1500.50)
    arroz = Compra(maria, datetime.now(), 500.00)
    feijao = Compra(maria,datetime(2018, 6, 4), 200.00)
    danilo.registra_compra(arroz)
    danilo.registra_compra(feijao)

    print(f'Cliente: {danilo.nome} ', '(adulto)' if danilo.is_Adulto() else '')
    print(f'Vendedor: {arroz.vendedor.nome}')
    print(f'Valor total das compras: {danilo.total_compras()}')
    print(f'Data da ultima compra: {danilo.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()
