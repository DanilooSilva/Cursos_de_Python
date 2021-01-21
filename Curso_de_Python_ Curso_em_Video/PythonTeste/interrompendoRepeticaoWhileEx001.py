cont = soma = 0
while True:
    numero = int(input(f'Digite {cont + 1}° valor: (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'A soma dos {cont} valores é {soma}')