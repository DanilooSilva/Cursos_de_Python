palavra_secreta = 'teste'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1 or letra.isnumeric():
        print('Ahh isso não vale digite apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in palavra_secreta:
        print(f'Uhuuull, a letra "{letra} existe na palavra secreta.')
    else:
        print(f'AFFzzz: a letra "{letra}" NÂO EXISTE na palavra secreta.')
        digitadas.pop()
        chances -= 1

    secreta = ''
    for le in palavra_secreta:
        if le in digitadas:
            secreta += le
        else:
            secreta += '*'

    if secreta == palavra_secreta:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreta}')
        break
    else:
        print(f'A palavra secreta está assim: {secreta}')

    print(f'Você ainda tem {chances} chances.')
    print()