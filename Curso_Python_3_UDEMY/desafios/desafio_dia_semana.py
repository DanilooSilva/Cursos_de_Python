def get_dia_semana(dia):
    dias = {
        (1, 7): 'fim-de-semanda',
        tuple(range(2, 7)): 'semana'
    }
    dia_escolhido = (tipo for numero, tipo in dias.items() if dia in numero)
    return next(dia_escolhido, '** dia inválido ***')


print(get_dia_semana(2))