from random import randint
cont = 0
while True:
    pc = randint(0, 9)
    hm = int(input('Digite um valor: '))
    hmEscolhe = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while hmEscolhe not in 'PI':
        hmEscolhe = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = pc + hm
    if soma % 2 == 0:
        if hmEscolhe in 'P':
            print(f'Você jogou {hm} e o computador {pc}. Total de {soma} DEU PAR')
            print('Você Venceu!!')
            cont += 1
        else:
            print(f'Você jogou {hm} e o computador {pc}. Total de {soma} DEU PAR')
            print('Você Perdeu!!')
            break
    else:
        if hmEscolhe in 'I':
            print(f'Você jogou {hm} e o computador {pc}. Total de {soma} DEU Ímpar')
            print('Você Venceu!!')
            cont += 1
        else:
            print(f'Você jogou {hm} e o computador {pc}. Total de {soma} DEU Ímpar')
            print('Você Perdeu!!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over!', end=' ')
print(f'Você venceu {cont} vez(es)' if cont > 0 else 'Você não venceu nenhuma vez')