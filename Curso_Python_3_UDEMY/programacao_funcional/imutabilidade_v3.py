from functools import reduce
from operator import add

valores = (30, 10, 25, 70, 100, 94)

print(tuple(sorted(valores)))
print(valores)

# valores.sort(reverse=True)
# print(valores)

print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(tuple(reversed(valores)))
# valores.reverse()
# print(valores)