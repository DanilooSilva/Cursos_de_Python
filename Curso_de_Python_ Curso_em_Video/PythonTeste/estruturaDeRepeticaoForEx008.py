palavra = str(input('Digite uma frase: ')).strip().upper()
frase = palavra.split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == palavra:
    print('é um palindroma')
else:
    print('não é um palindroma')
