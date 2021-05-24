"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

"""
from dados import *
import json

# lista = [1, 2, 3, 4, 5, 6]
# dados_json = json.dumps(clientes_dicionario, indent=4)
# print(dados_json)

# dicionario = json.loads(clientes_json)
# for v in dicionario.values():
#     for key, value in v.items():
#         print(f'{key}: {value}')
#     print('---'*15)

# criando um arquivo
# with open(r'aula132\clientes.json', 'w') as arquivo:
#     json.dump(clientes_dicionario, arquivo, indent=4)

#lendo um arquivo
with open(r'aula132\clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)