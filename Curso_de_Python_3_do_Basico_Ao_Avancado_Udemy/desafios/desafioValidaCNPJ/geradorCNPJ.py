from random import randint
from desafioValidaCNPJ import validadorSegundoDigito


def get_CNPJ():
    return formmata_novo_cnpj(validadorSegundoDigito(concatena_mil_contra(get_oito_primeiros)))


def get_oito_primeiros():
    primeiro_digito = randint(0, 9)
    segundo_digito = randint(0, 9)
    segundo_bloco = randint(100, 999)
    terceiro_bloco = randint(100, 999)
    oito_primeiros = str(primeiro_digito) + str(segundo_digito) \
        + str(segundo_bloco) + str(terceiro_bloco)
    return oito_primeiros


def concatena_mil_contra(oito_primeiros):
    doze_primeiros = oito_primeiros() + '0001'
    return doze_primeiros


def formmata_novo_cnpj(args):
    cnpj_formatado = ''
    for c in range(0, len(args)):
        if c < 2 or c > 2 and c < 5 or c > 5 and c < 8 or c > 8 and c < 12 or c > 12:
            cnpj_formatado += args[c]
        elif c == 2 or c == 5:
            cnpj_formatado += '.' + args[c]
        elif c == 8:
            cnpj_formatado += '/' + args[c]
        elif c == 12:
            cnpj_formatado += '-' + args[c]
    return cnpj_formatado


if __name__ == '__main__':
    print(get_CNPJ())
