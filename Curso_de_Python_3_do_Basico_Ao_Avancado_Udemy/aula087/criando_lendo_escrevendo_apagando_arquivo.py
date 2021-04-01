file = open('aula87\\abc.txt', 'w+')
for numero in range(0 , 3):
    file.write(f'linha {numero}\n')

file.seek(0, 0) # volta para posição relativa
print(file.read())

file.seek(0, 0)
print('#######')
for linha in file.readlines():
    print(linha, end='')

file.close()