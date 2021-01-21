string = '01234567890123456789012345678901234567890123456789'
n = 10
lista = [string[i:i + n] for i in range(0, len(string), n)]
string_formatada = '.'.join(lista)
print(string_formatada)