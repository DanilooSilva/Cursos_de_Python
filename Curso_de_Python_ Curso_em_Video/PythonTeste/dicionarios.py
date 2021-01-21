'''
pessoas = {
   'nome': 'Danilo', 'sexo': 'M', 'idade': 26
}
print(pessoas)
print()
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print()
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
for k in pessoas.keys():
   print(k)
print()
for k in pessoas.values():
   print(k)
print()
for k, v in pessoas.items():
   print(f'{k} = {v}')
print()
del pessoas['sexo']
print(pessoas)
print()
pessoas['nome'] = 'Leandro'
print(pessoas)
print()
pessoas['peso'] = 98.5
print(pessoas)
'''
'''
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['uf'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
   estado['uf'] = str(input('Unidade Federativa: '))
   estado['sigla'] = str(input('Sigla do Estado: '))
   brasil.append(estado.copy())
print(brasil)

for e in brasil:
   print(e)
for e in brasil:
   for k, v in e.items():
      print(f'O campo {k} tem o valor {v}')