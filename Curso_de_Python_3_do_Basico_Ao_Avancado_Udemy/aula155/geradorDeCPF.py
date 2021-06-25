from random import randint

def gera_cpf():
    numero = str(randint(100000000, 999999999))
    novo_cpf = numero
    digito1 = 0
    digito2 = 0
    for index, numero in enumerate(range(10, 1, -1)):
        digito1 += int(novo_cpf[index]) * numero
    digito1 = 11 - (digito1 % 11)
    digito1 = digito1 if digito1 <= 9 else 0

    novo_cpf += str(digito1)

    for index, numero in enumerate(range(11, 1, -1)):
        digito2 += int(novo_cpf[index]) * numero
    digito2 = 11 - (digito2 % 11)
    digito2 = digito2 if digito2 <= 9 else 0 

    novo_cpf += str(digito2)
    return novo_cpf
