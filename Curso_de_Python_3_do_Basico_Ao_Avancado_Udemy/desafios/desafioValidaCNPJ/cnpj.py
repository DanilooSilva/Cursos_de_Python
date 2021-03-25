def validador(cnpj):
    cnpj_original = removeCaracteresEspeciais(cnpj)
    cnpj = cnpj_original
    if getCNPJString(validadorSegundoDigito(cnpj)) == cnpj_original:
        return True
    return False
    
    
    
def validadorPrimeiroDigito(cnpj):
    cnpj = getCNPJlista(cnpj)
    cnpj.append(formula(calculoPrimeiroDigito(cnpj)))
    return cnpj


def getCNPJlista(cnpj):
    return [cnpj[c] for c in range(0, len(cnpj) - 2)]


def getCNPJString(cnpjLista):
    cnpj = ''
    for c in cnpjLista:
        cnpj += c
    return cnpj


def calculoPrimeiroDigito(cnpj):
    lista_ajuda_calculo = [x for x in range(5, 1, -1)]
    lista_ajuda_calculo += [x for x in range(9, 1, -1)]
    resultado = 0
    for x in range(0, len(lista_ajuda_calculo)):
        resultado += lista_ajuda_calculo[x] * int(cnpj[x])
    return resultado


def validadorSegundoDigito(cnpj):
    cnpj = validadorPrimeiroDigito(cnpj)
    cnpj.append(formula(calculoSegundoDigito(cnpj)))
    return cnpj


def calculoSegundoDigito(cnpj):
    lista_ajuda_calculo = [x for x in range(6, 1, -1)]
    lista_ajuda_calculo += [x for x in range(9, 1, -1)]
    resultado = 0
    for x in range(0, len(lista_ajuda_calculo)):
        resultado += lista_ajuda_calculo[x] * int(cnpj[x])
    return resultado


def removeCaracteresEspeciais(cnpj):
    return cnpj.replace('.','').replace('/','').replace('-', '')

def formula(resultado):
    return str(11 - (resultado % 11) if 11 - (resultado % 11) <= 9 else 0)

if __name__ == '__main__':
    print(validador('04.252.011/0001-10'))