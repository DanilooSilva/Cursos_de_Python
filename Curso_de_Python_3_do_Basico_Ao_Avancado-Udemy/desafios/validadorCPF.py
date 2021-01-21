cpf = ''
while True:
    cpf = input('CPF ###.###.###-## ou 000 para sair: ')
    if cpf == '000':
        break
    if len(cpf) < 14 or cpf.isnumeric():
        print('CPF Inválido!')
        continue
    cpf = cpf.replace('.', '').replace('-', '')
    calculo1 = 0
    for i, n in enumerate(range(10, 1, -1)):
        calculo1 += int(cpf[i]) * n

    calculo1 = 11 - (calculo1 % 11)
    calculo1 = calculo1 if calculo1 <= 9 else 0

    calculo2 = 0
    for i, n in enumerate(range(11, 1, -1)):
        calculo2 += int(cpf[i]) * n

    calculo2 = 11 - (calculo2 % 11)

    if int(cpf[-2]) == calculo1 and int(cpf[-1]) == calculo2:
        print('CPF Válido')
    else:
        print('CPF inválido')

    