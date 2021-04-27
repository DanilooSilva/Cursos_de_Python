from classes.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self._conta = conta

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta):
        self._conta = conta