def ficha(nome='<desconhecido>', gol='0'):
    print(f'O jogador {nome}, fez {gol} gol(s) no campeonato.')


print('--' * 30)
nomeJogador = str(input('Nome do jogador: ')).strip()
while True:
    gols = str(input('Números de Gols: '))
    if gols == '':
        gols = '0'
    if gols.isnumeric():
        if nomeJogador == '' and int(gols) > 0:
            ficha(gol=gols)
        elif nomeJogador != '' and int(gols) == 0:
            ficha(nome=nomeJogador)
        elif nomeJogador != '' and int(gols) > 0:
            ficha(nomeJogador, gols)
        else:
            ficha()
        break
    else:
        print('Erro, Favor passar números de gols.')