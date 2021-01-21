def voto(ano):
    """
    -> Verifica a obrigatoriedade de voto de uma pessoa
    :param ano: Ano de nascimento de uma pessoa
    :return: retonar se uma pessoa tem o voto NEGADO, OPCIONAL OU OBRIGATORIO
    Função desenvolvida por Danilo
    """
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade}: ', end='')
    if idade < 16:
        return 'Voto Negado!'
    elif idade < 18 or idade > 64:
        return 'Voto Opcional!'
    else:
        return 'Voto Obrigatório!'

help(voto)
anoNasc = int(input('Em que ano você nasceu? '))
print(voto(anoNasc))