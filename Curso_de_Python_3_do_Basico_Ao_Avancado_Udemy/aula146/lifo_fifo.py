"""
    Pilhas e filas
    Pilha (stack) - LIFE - last in, first out.
        Exemplo: Pilha de livros que são adicionados um sobre o outro
    Fila (queue) - FIFO - first in, first out. 
        Exemplo: uma fila de banco (oi qualquer fila de vida real)
    Fila podem ter efeitos colaterais em desempenho, porque a cada item
    alterado, todos os índice serão modificados. 
"""
# livros = list()
# livros.append('Livro 1')
# livros.append('Livro 2')
# livros.append('Livro 3')
# livros.append('Livro 4')
# livros.append('Livro 5')
# print(livros)
# livro_removido = livros.pop()
# print(livros)
# print(livro_removido)

from collections import deque
fila = deque()
fila.append('Danilo')
fila.append('Maria')
fila.append('Allanys')
fila.append('Scarlett')
fila.append('Ohara')
fila.append('Mel')
fila.popleft()
print(fila)
