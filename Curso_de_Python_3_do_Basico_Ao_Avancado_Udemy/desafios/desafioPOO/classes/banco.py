class Banco:
    def __init__(self):
        self.__contas = []
        self.__clientes = []
    
    def add_cliente(self, cliente):
        if cliente in self.__clientes:
            print('Cliente já existente')
        self.__clientes.append(cliente)
        
    def add_conta(self, conta):
        if conta in self.__contas:
            print('Conta já existente')
        self.__contas.append(conta)

    def valida(self, conta, cliente, agencia):
        if self.__valida_conta(conta) and self.__valida_agencia(agencia) and self.__valida_cliente(cliente):
            return True
        return False

    def __valida_conta(self, conta):
        if  conta in self.__contas:
            return True
        return False

    def __valida_agencia(self, agencia):
        if agencia in self.__get_agencias():
            return True
        return False

    def __valida_cliente(self, cliente):
        if cliente in self.__clientes:
            return True
        return False

    def __get_agencias(self):
        agencias = []
        for c in self.__contas:
            agencias.append(c.agencia)
        return agencias
