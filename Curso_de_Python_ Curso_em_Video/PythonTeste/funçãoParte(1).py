# def soma (a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma de A + B = {s}')
#
#
# soma(4, 5)
# def contador(* num):
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} números')
#
#
# contador(1, 2, 3)
# contador(4, 5, 1, 4, 5)
# contador(9, 1, 8, 8, 7, 5, 6)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 5, 9, 1, 0, 2]
dobra(valores)
print(valores)