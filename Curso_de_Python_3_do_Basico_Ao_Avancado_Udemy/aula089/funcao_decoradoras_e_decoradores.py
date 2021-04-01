def master(funcao):
    def slave(*args, **kwargs):
        print('Afora estou decorada')
        funcao(*args, **kwargs)
    return slave


@master
def fala_oi():
    print('Oi')

@master
def outra_funcao(msg):
    print(msg)

#fala_oi = master(fala_oi)

fala_oi()

outra_funcao('Sou Danilo Gomes')
