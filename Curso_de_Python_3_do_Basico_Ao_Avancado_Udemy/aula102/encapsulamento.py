"""
    Public, Protected, Private

    _ protected
    __ private (_NOMECLASSE__nomeatributo)
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Danilo')
bd.inserir_cliente(2, 'Maria')
bd.inserir_cliente(3, 'Allanys')
bd.inserir_cliente(4, 'Scarlett')
bd.apaga_cliente(3)
bd.lista_clientes()
