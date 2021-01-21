valorCasa = float(input('Informe o valor da casa R$: '))
valorSalario = float(input('Informe o valor do seu salário R$: '))
quantidadeParcelas = int(input('Infome a quantidade de parcelas: '))

prestacao = valorCasa / quantidadeParcelas
anos = int(quantidadeParcelas / 12)
meses = int(quantidadeParcelas % 12)

if prestacao < (valorSalario * 30) / 100:
    print('Emprestimo pode ser realizado! ')
else:
    print('Emprestimo Negado!')
    print('O valor da parcela do emprestimo está acima de 30% do seu salário.')


print('O valor da parcela R$ {:.2f} em {} ano(s) e {} mes(es)'.format(prestacao, anos, meses))