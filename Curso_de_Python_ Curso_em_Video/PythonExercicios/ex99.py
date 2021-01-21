from time import sleep
def maior(* num):
    print('-=' * 30)
    sleep(0.5)
    print('Analisando os valores passados.....')
    for v in num:
        print(f'{v} ', end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} ao todo')
    sleep(0.3)
    print(f'O maior número informado foi {max(num)}.')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
#maior()