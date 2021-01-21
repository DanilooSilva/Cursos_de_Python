def escreva(txt):
    tm = len(txt) + 4
    print('~' * tm)
    print(f'{txt:^{tm}}')
    print('~' * tm)

escreva('Olá Mundo')
escreva('M')