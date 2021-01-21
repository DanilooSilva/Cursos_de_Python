def conceitos(nota=0):
    if nota > 10 or nota < 0:
        print('Nota inválida')
    elif nota > 9:
        return 'A'
    elif nota > 8:
        return 'A-'
    elif nota > 7:
        return 'B'
    elif nota > 6:
        return  'B-'
    elif nota > 5:
        return 'C'
    elif nota > 4:
        return 'C-'
    elif nota > 3:
        return 'D'
    elif nota > 2:
        return 'D-'
    elif nota > 1:
        return 'E'
    else:
        return 'E-'


if __name__ == '__main__':
    while True:
        try:
            nota = float(input('Digite a nota: '))
        except:
            print('Valor inserido incorreto!')
        else:
            conceito = conceitos(nota)
            if conceito is not None:
                print(f'Sua nota é equivalente a {conceito}')

        continuar = ''
        while True:
            continuar = str(input('Desejá inserir outra nota? [S/N]: ')).strip()[0].upper()
            if continuar in 'SN':
                break
        if continuar in 'N':
            break
    print('FIM')
