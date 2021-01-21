# def contador(i, f, p):
#     """
#         -> Faz um contagem e mostra na tela.
#         :param i: inicio da contagem
#         :param f: Fim da contagem
#         :param p: Passo da contagem
#         :return: Sem retorno
#         Função criada por Danilo
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end=' ')
#         c += p
#     print('Fim!')
#
#
# contador(2, 10, 2)
#
# help(contador)

# def somar(a=0, b=0, c=0):
#     """
#     ->Faz a soma de três valores e mostra o resultado na tela
#     :param a: o primeiro valor
#     :param b: O segundo valor
#     :param c: O terceiro valor
#     :return: Função sem retorno
#     Função criada por Danilo Gomes
#     """
#     s = a+b+c
#     print(f'A soma vale {s}')
#
# somar(3,2,5)
# somar(8, 4)
# somar(a=3, c=2)


# def soma(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
#
# r1 = soma(2, 3, 4)
# r2 = soma(2, 2)
# r3 = soma(6)
#
#
# print(f'Os resultados foram {r1}, {r2} e {r3}')




def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')