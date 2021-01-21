from datetime import date
dados = {}
nome = str(input('Nome: ')).strip().title()
anoNasc = int(input('Ano de Nascimento: '))
ctps = int(input('Carteira de Trabalho (0 não tem): '))
anoContratacao = salario = 0
idade = date.today().year - anoNasc
dados['nome'] = nome
dados['idade'] = idade
dados['ctps'] = ctps
if ctps > 0:
    anoContratacao = int(input('Ano de Contratação: '))
    salario = float(input('Salario: '))
    dados['contratacao'] = anoContratacao
    dados['salario'] = salario
    contribuicao = date.today().year - anoContratacao
    dados['aposentadoria'] = idade - contribuicao + 35
print('-=' * 30)
for chave, valor in dados.items():
    print(f'{chave} tem o valor {valor}')