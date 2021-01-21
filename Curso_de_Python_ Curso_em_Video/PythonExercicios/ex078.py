valores = list()
maior = menor = 0
for index in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {index}: ')))
print('-=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for index, valor in enumerate(valores):
    maior = max(valores)
    if valor == maior:
        print(f'{index}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições', end='')
for index, valor in enumerate(valores):
    menor = min(valores)
    if valor == menor:
        print(f' {index}... ', end='')
