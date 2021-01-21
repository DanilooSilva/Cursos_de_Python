from time import sleep
def maior(* num):
    sleep(0.3)
    print('-=' * 30)
    print('Analisando os valores passados....')
    for n in num:
        sleep(0.3)
        print(f'{n}', end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(0.3)
    print(f'O maior valor informado foi {max(num)}')


maior(2, 9, 4, 5, 7, 1)
sleep(0.3)
maior(4, 7, 0)
sleep(0.3)
maior(1, 2)
sleep(0.3)
maior(6)
sleep(0.3)
maior(0)