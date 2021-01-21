jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: ')).strip()
qntjogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for qnt in range(1, qntjogos +1):
    gols.append(int(input(f'Quantos gols na partida {qnt}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {qntjogos} partidas.')
for j, g in enumerate(jogador['gols']):
    print(f'{"=>":>10} na partida {j + 1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')