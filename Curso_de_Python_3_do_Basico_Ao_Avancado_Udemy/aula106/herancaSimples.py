from classes import Cliente, Pessoa, Aluno

"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança É

"""

c1 = Cliente('Danilo', 27)
print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 27)
print(a1.nome)
a1.falar()
a1.estudar()