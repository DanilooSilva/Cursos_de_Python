def leiaInt(mgn):
    ok = False
    while True:
        n = str(input('Digite um número: '))
        if n.isnumeric():
            valor = int(n)
            ok = True
            return valor
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
        if ok is True:
            break



n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
