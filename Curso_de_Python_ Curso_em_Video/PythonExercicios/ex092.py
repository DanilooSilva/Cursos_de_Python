from datetime import date
anoAtual = date.today().year
dados = {}
dados['nome'] = str(input('Nome: ')).strip()
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = anoAtual - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] > 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['aposentadoria'] = (anoAtual - nascimento) - (anoAtual - dados['contratacao']) + 35
print('-=' * 30)
for k, v in dados.items():
    print(f'{" - ":>10}{k} tem o valor {v}')