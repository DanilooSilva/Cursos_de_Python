numero = int(input('Digite um número: '))

escolha = int(input('\033[31m1 para Binario\033[m, \033[32m2 para Octal\033[m, \033[33m3 para Hexadecimal\033[m:'))

if escolha == 1:
    binario = bin(numero)
    print('O numero {} em binário é {}'.format(numero, binario[2:]))
elif escolha == 2:
    octal = oct(numero)
    print('O numero {} em Octal é {}'.format(numero, octal[2:]))
elif escolha ==3:
    hexa = hex(numero)
    print('O numero {} em Hexadecimal é {}'.format(numero, hexa[2:]))
else:
    print('Opção invalida')
