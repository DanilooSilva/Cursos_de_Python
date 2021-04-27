#from conta import Conta
from classes.conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero, agencia, saldo=0):
        super().__init__(numero, agencia, saldo)

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            raise ValueError("Saldo Insuficiente")
        
        self.extrato(valorSacado=valor, valorDeposito=0)

    def extrato(self, valorSacado=0, valorDeposito=0):
        print('*+' * 30)
        if valorSacado > 0:
            print(f'{"Valor do Saque: ":<30} R$ {valorSacado:.2f}')
        print(f'{"Saldo: ":<30} R$ {self._saldo:.2f}')
        print('*+' * 30)



if __name__ == '__main__':
    cp = ContaPoupanca('12345', '678910')
    cp.depositar(1500)
    cp.sacar(100)