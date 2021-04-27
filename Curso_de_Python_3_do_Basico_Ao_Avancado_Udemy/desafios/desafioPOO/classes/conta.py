from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @property
    def numero(self):
        return self._agencia

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if not isinstance(saldo, (float, int)):
            raise ValueError("Saldo precisa ser númerico")

        self._saldo = saldo

    def depositar(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError("Valor para deposíto precisa ser númerico")
        
        if valor > 0:
            self._saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def extrato(self, valorSacado=0, valorDeposito=0):
        pass
    