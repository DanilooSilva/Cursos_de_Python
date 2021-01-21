class Carro:
    def __init__(self, velocidadeMaxima):
        self.velocidadeMaxima = velocidadeMaxima
        self.velocidade = 0

    def acelerar(self, delta=5):
        if self.velocidade < self.velocidadeMaxima:
            self.velocidade += delta
        else:
            self.velocidade = 180
        return self.velocidade if self.velocidade <= self.velocidadeMaxima else 180

    def frear(self, delta=20):
        if self.velocidade > 0:
            self.velocidade -= delta
        else:
            self.velocidade = 0
        return self.velocidade if self.velocidade >= 0 else 0


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(f'Acelerando {c1.acelerar(8)}')

    for _ in range(10):
        print(f' reduzindo a velocidade {c1.frear(delta=20)}')