from random import randint
print('-=-' * 30)
print('Vamos Jogar Par ou Ímpar')
print('-=-' * 30)
print()
vitoria = soma = 0
while True:
    pc = randint(0, 10)
    print('*-*' * 30)
    hu = int(input('Diga um valor: '))
    parImpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('*-*' * 30)
    soma = pc + hu
    if soma != 2 == 0:
        if parImpar == 'P':
            print(f'Você jogou {hu} e o computador {pc}. Total de {soma} deu PAR')
            vitoria += 1
        else:
            print('Você Perdeu')
            print(f' Voce jogou {hu} e o computador {pc}. Total de {soma} de Ímpar')
            break
    else:
        if parImpar == 'I':
            print(f'Voce jogou {hu} e o computador {pc}. Total de {soma} deu Ímpar')
            vitoria += 1
        else:
            print('Você Perdeu')
            print(f' Voce jogou {hu} e o computador {pc}. Total de {soma} de Ímpar')
            break
print('-=-' * 30)
print(f'GAME OVER! Você venceu {vitoria} vez(es).')