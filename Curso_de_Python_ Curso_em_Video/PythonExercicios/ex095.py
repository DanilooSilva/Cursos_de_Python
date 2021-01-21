time = []
jogador = {}
gols = []
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    qntjogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for qnt in range(1, qntjogos +1):
        g = int(input(f'Quantos gols na partida {qnt}? '))
        gols.append(g)
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    time.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        print('Erro! Digite S ou N!')
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print('Cod ', end='')
for c in time[0].keys():
    print(f'{c.title():<15} ', end='')
print()
print('-' * 50)
for i, vl in enumerate(time):
    print(f'{i:>3} ', end='')
    for v in vl.values():
        print(f'{str(v):<15} ', end='')
    print()
while True:
    print('-' * 50)
    jo = int(input('Mostar dados de qual jogador? (999 para parar): '))
    if jo == 999:
        break
    elif jo <= len(time):
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[jo]["nome"]}')
        for j, gl in enumerate(time[jo]['gols']):
            print(f'{"No jogo":>15} {j + 1} fez {gl} gols.')
    else:
        print(f'Erro! Não existe jogador com o codigo {jo}!')
print('<<< VOLTE SEMPRE" >>>')
