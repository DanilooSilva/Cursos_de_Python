soma = 0
mult = 0
opc = 0
while opc != 5:
    numero = float(input('Digite um valor: '))
    numero2 = float(input('Digite outro valor: '))
    print('''
    [1] Somar
    [2] Multiplicar 
    [3] Maior
    [4] Novos números
    [5] sair
    ''')
    opc = int(input('Qual opção: '))
    if opc == 1:
        soma = numero + numero2
        print('A soma de {} + {} = {}'.format(numero, numero2, soma))
        opc = 5
    elif opc == 2:
        mult = numero * numero2
        print('A multiplicação de {} * {} = {}'.format(numero, numero2, mult))
        opc = 5
    elif opc == 3:
        if numero > numero2:
            print('O maior número é {}'.format(numero))
        else:
            print('O maior número é {}'.format(numero2))
        opc = 5