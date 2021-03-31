
class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


if __name__ == '__main__':
    p1 = Pessoa('Danilo', 27)
    p1.get_ano_nascimento()

    p2 = Pessoa.por_ano_nascimento('Maria', 1992)
    print(p2.nome, p2.idade)
