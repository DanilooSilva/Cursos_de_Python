def leiaInt(mgn):
    while True:
        try:
            n = int(input(mgn))
        except (ValueError, TypeError):
            print('Erro: Digite um número inteiro válido')
        except Exception as erro:
            print(erro.__cause__, erro.__class__)
        else:
            return  n
            break


def leiaReal(mgn):
    while True:
        try:
            f = float(input(mgn))
        except (ValueError, TypeError):
            print('Erro: Digite um número real válido')
        except Exception as erro:
            print(erro.__cause__, erro.__class__)
        except KeyboardInterrupt:
            f = 0
            return f
            break
        else:
            return f
            break



i = leiaInt('Digite um número Inteiro:  ')
f = leiaReal('Digite um número Real: ')
print(f'O valor inteiro digitado foi {i} e o valor rela foi {f}')