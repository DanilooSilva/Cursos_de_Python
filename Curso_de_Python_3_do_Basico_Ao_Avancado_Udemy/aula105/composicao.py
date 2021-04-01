
from classes import Cliente


cliente1 = Cliente('Danilo', 27)
cliente1.insere_endereco('Osasco', 'SP')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Maria', 28)
cliente2.insere_endereco('São Paulo', 'SP')
cliente2.insere_endereco('Belo Horizonte', 'MG')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Ohara', 2)
cliente3.insere_endereco('Rio de Janeiro', 'Rj')
print(cliente3.nome)
cliente3.lista_enderecos()
