salario = float(input('Digite o valor do Salario '))


if salario > 1250:
    novoSalario = ((salario * 10) / 100) + salario
    print('Seu novo salario é R$ {:.2f}'.format(novoSalario))
else:
    novoSalario = ((salario * 15) / 100) + salario
    print('Seu novo salario é R$ {:.2f}'.format(novoSalario))
