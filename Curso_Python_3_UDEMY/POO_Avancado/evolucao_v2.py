#! python3

class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Austrolopiteco', ) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSpaiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSpaiens('José')
    grokn = Neanderthal('Grokn')

    print(f'Evolução (a partir da Classe): {", ".join(HomoSpaiens.especies())}')
    print(f'Evolução (a partir da instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluido? {HomoSpaiens.is_evoluido()}')
    print(f'Neanderthal evoluído? {Neanderthal.is_evoluido()}')
    print(f'José evoluido? {jose.is_evoluido()}')
    print(f'Grokn evoluído? {grokn.is_evoluido()}')