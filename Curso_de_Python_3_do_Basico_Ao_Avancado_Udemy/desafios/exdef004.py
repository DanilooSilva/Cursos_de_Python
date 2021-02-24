"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, returne Fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função for
fivissível por 5 e por 3, return FizzBuzz, caso contrário, retorne o número enviado.
"""


def fizzBuzz(valor):
    if valor % 3 == 0 and valor % 5 == 0:
        return 'FizzBuzz'
    if valor % 5 == 0:
        return 'Buzz'
    if valor % 3 == 0:
        return 'Fizz'
    return f'{valor}'


print(fizzBuzz(15))
print(fizzBuzz(7))
print(fizzBuzz(10))
print(fizzBuzz(9))