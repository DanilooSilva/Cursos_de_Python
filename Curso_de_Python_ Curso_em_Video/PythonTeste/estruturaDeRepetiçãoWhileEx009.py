continuar = ''
cont = 1
soma = 0
media = 0
maior = 0
menor = 0
while continuar != 'N':
    n = float(input('Digite um valor: '))
    if cont == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    cont += 1
    continuar = str(input('Deseja continuar: [s/n] ')).strip().upper()
media = soma / cont
print('A soma de todos os valores é {}'.format(soma))
print('A média dos valores é {:.1f}'.format(media))
print('O maior númerio digitado {:.1f} O menor número digitado {:.1f}'.format(maior, menor))
