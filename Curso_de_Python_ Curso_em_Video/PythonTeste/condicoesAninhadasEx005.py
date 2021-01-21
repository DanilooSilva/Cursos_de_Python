semestre1 = float(input('Digite a nota do 1° semestre: '))
semestre2 = float(input('Digite a nota do 2° semestre: '))

media = (semestre1 + semestre2) / 2

if media < 5:
    print('\033[31mReprovado\033[m')
elif media <= 6.9:
    print('\033[33mRecuperação\033[m')
else:
    print('\033[32mAprovado\033[m')