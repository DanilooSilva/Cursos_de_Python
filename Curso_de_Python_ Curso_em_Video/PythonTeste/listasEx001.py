numeros = list()
for valores in range(0, 5):
    numeros.append(int(input(f'Digite um valor para Posição {valores}: ')))
maiorValor = numeros[0]
posicaoMaior = 0
menorValor = numeros[0]
posicaoMenor = 0

print(f'Você digitou os valores {numeros}')

for index, valor in enumerate(numeros):
    if valor > maiorValor:
        maiorValor = valor
        posicaoMaior = index
    if valor < menorValor:
        menorValor = valor
        posicaoMenor = index

print(f'O maior valor digitado foi {maiorValor} na posição', end=' ')
for posicao, n in enumerate(numeros):
    if n == maiorValor:
        print(f'{posicao}...', end=' ')
print(f'\nO Menor valor digitado foi {menorValor} na posição', end=' ')
for posicao, n in enumerate(numeros):
    if n == menorValor:
        print(f'{posicao}...', end=' ')