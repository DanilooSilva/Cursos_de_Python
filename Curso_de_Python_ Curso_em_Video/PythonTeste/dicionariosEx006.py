jogadores = []
jogador = {}
gols = []
somagols = gol = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for p in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {p + 1}? '))
        somagols += gol
        gols.append(gol)
    jogador['gols'] = gols[:]
    gols.clear()
    jogador['total'] = somagols
    jogadores.append(jogador.copy())
    jogador.clear()
    somagols = 0
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break

print('-=' * 30)
print(jogadores)
print('-=' * 30)
print(f'{"Cod":>3} ', end='')
for i in jogadores[0].keys():
    print(f'{i.title():<14} ', end='')
print()
print('_' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    mostrar = int(input('Mostrar dados de qual jogador? '))
    if mostrar == 999:
        break
    while mostrar > len(jogadores):
        mostrar = int(input('ERRO! Não existe o jogador com o código {mostrar}! Tente novamente! '))
    print(f'-- Levantamento do jogador {jogadores[mostrar]["nome"]}')
    for i, go in enumerate(jogadores[mostrar]["gols"]):
        print(f'{"   No jogo " + str(i + 1) + " fez " + str(go) + " gol(s) "}')
print('<<< Volte sempre >>>')