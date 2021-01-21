salario = float(3450.45)
despesas = float(2456.2)

percentual = despesas * 100 / salario
per = str(percentual).replace('.', ',')
print(f'{per}%')

