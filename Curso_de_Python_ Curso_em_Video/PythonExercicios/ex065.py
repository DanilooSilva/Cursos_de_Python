continuar = 's'
cont = media = soma = numero = maior = menor = 0
while continuar not in 'Nn':
    numero = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [s/n] ')).strip().upper()[0]
    cont += 1
    soma += numero
    if cont == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))