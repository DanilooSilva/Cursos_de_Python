#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

menu = 0
num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))
while menu != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    menu = int(input('>>>>>> Qual é sua Opção? '))
    if menu == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    elif menu == 2:
        print('{} * {} = {}'.format(num1, num2, num1 * num2))
    elif menu == 3:
        if num1 > num2:
            print('O maior número é {}'.format(num1))
        elif num1 < num2:
            print('O maior número é {}'.format(num2))
        else:
            print('Os dois número são iguais!')
    elif menu == 4:
        num1 = float(input('Primeiro valor: '))
        num2 = float(input('Segundo valor: '))
    elif menu == 5:
        print('Saindo !')
    else:
        print('Opção inválida')
    print('-=-' * 30)
print('Fim do programa! Volte sempre...')