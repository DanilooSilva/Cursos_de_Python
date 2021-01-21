aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]} '))
if aluno['media'] < 6:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igula a {aluno["media"]}')
print(f'Situação é igual a {aluno["situacao"]}')