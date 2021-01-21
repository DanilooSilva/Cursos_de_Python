def voto(aN):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - aN
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'NÃO VOTA!'
    elif idade >= 16 and idade < 18 or idade > 65:
        return 'VOTO OPCIONAL!'
    else:
        return 'VOTO OBRIGATÓRIO'



print(voto(2018))