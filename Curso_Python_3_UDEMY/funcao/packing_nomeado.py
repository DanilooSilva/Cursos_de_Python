def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao.ljust(10)} -> {piloto.ljust(40)}')


if __name__ == '__main__':
    resultado_f1(pimeiro='L. Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')