import re

def valida_cpf(cpf):
    cpf = str(cpf)

    cpf = re.sub(r'[^0-9]', '', cpf)    
    novo_cpf = cpf[:-2]

    if not cpf or len(cpf) != 11:
        return False

    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11

            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    if cpf == novo_cpf:
        return True
    else:
        return False
