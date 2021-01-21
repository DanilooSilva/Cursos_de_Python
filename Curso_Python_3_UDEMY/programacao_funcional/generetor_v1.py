#! python3
def cores_arco_ires():
    yield 'Vermelho'
    yield 'Laranja'
    yield 'Amarelo'
    yield 'Verde'
    yield 'Azul'
    yield 'Índigo'
    yield 'Violeta'


if __name__ == '__main__':
    generator = cores_arco_ires()
    print(type(generator))
    while True:
        print(next(generator))