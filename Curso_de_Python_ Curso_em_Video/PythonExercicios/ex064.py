numero = 0
soma = 0
cont = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero < 999:
        soma += numero
        cont += 1
print('Você digitou {} número(s) e a soma entre ele(s) foi {}'.format(cont, soma))