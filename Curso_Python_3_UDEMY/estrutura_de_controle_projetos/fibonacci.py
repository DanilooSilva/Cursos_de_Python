def fibonacci(quantidade):
    resultado = [0, 1]
    for i in range(len(resultado), quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)