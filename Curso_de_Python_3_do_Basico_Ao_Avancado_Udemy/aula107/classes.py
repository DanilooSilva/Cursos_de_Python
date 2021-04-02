class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    def falar(self):
        print(f'{self.nome_classe} está Falando!')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_classe} Compando...')

    def falar(self):
        print('Estou em Cliente!')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_classe} estudando...')


class ClienteVIP(Cliente):
    # def falar(self):
    #     Pessoa.falar(self)
    #     Cliente.falar(self)
    #     print(f'{self.nome_classe} Outra coisa qualquer')
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome
    
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')