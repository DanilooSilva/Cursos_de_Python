def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita vários)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    situ = {}
    situ['total'] = len(n)
    situ['maior'] = max(n)
    situ['menor'] = min(n)
    situ['media'] = sum(n) / len(n)
    if sit:
        if situ['media'] >= 7:
            situ['situação'] = 'OTIMA!'
        elif situ['media'] >= 5:
            situ['situação'] = 'BOA!'
        else:
            situ['situação'] = 'RUIM!'
    return situ


# resp = notas(5.5, 2.5, 9, 8.5)
# print(resp)
help(notas)