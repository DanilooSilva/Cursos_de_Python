def leiaInt(mgn):
    print('-' * 30)
    while True:
        n = str(input(mgn))
        if n.isnumeric():
            return n
            break
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')



n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')