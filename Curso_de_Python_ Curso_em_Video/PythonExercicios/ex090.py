aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do {aluno["nome"].title()} '))
while aluno['media'] > 10:
    aluno['media'] = float(input('Não é possível que a média de aluno seja maior que 10. Favor digitar novamente: '))
if aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado!'
else:
    aluno['situacao'] = 'Aprovado!'
print('-=' * 40)

for c, v in aluno.items():
    print(f' {"- ":>10}  {c.title()} é igual {str(v).title()}')