from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 30)
    sleep(0.4)
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} em {passo}')
    if inicio < fim:
        for v in range(inicio, fim + 1, passo):
            print(f'{v} ', end='')
            sleep(0.4)
        print('FIM!')
    else:
        for v in range(inicio, fim - 1, - passo):
            print(f'{v} ', end='')
            sleep(0.4)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)