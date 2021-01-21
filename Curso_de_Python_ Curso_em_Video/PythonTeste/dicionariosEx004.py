jogador = {}
gols = []
somagols = gol = 0
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {p + 1}? '))
    somagols += gol
    gols.append(gol)
jogador['gols'] = gols[:]
jogador['total'] = somagols
print('-=' * 30)
print(jogador)
print('-=' * 30)
for chave, valor in jogador.items():
    print(f'O campo {chave.title()} tem o valor {valor}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'{"Na partida "+str(i + 1)+", fez "+str(v)+" gol(s).":>30}')
print(f'Foi um total de {somagols} gol(s).')