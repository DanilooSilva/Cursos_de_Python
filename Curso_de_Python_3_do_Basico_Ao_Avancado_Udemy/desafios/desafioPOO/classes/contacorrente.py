#from conta import Conta
from classes.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, numero, agencia, saldo=0):
        super().__init__(numero, agencia, saldo)
        self.__limite = 1500.00

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor para saque precisa ser númerico")

        saldo_atual = float(self._calcula_Saldo_Total())

        if valor <= saldo_atual:
            self._saldo -= valor
            if self._saldo < 0:
                self.__limite += self._saldo
                self._saldo = 0
            self._calcula_Saldo_Total()
        else:
            raise ValueError("Saldo insuficiente.")

        self.extrato(valorSacado=valor)

    def extrato(self, valorSacado=0, valorDeposito=0):
        print('*+' * 30)
        if valorSacado > 0:
            print(f'{"Valor do Saque: ":<30} R$ {valorSacado:.2f}')
        print(f'{"Saldo: ":<30} R$ {self._saldo:.2f}')
        print(f'{"Saldo Limite: ":<30} R$ {self.__limite:.2f}')
        print(f'{"Total: ":<30} R$ {self._calcula_Saldo_Total()}')
        print('*+' * 30)

    def _calcula_Saldo_Total(self):
        saldo_total = self.__limite + self._saldo
        return f'{saldo_total:.2f}'


if __name__ == '__main__':
    cc = ContaCorrente('12345', '678910')
    cc.depositar(1500)
    cc.sacar(1700)
    
