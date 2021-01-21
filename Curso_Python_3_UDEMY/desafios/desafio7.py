PALAVRAS_PROIBIDAS = ['Futebol', 'Religião', 'Politica']
textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida'
]

for texto in textos:
    for palavra in texto.title().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f'A palavra {palavra} existe no texto ')
            break
    else:
        print(f'Não á palavras proíbidas no texto: {texto}')