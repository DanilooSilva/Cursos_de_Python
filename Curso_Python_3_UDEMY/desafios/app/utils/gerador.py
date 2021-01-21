def novo_nome():
    from random import randint
    nomes = ['Danilo', 'Maria', 'Allanys', 'Scarlett', 'Ohara', 'Mel']
    posicao_nomes = randint(0, len(nomes))
    return nomes[posicao_nomes]


if __name__ == '__main__':
    nome = novo_nome()
    print(nome)