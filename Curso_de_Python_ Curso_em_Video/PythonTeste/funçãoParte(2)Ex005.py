def nota(* notas, sit=False):
    """
    ->Função para analisar notas e situação de vários aluno.
    :param notas: Uma ou mais notas dos alunos (aceita váriaveis)
    :param sit: valor opcional, indica se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação do aluno.
    """
    print('--' * 30)
    enotas = {}
    cont = soma = 0
    for n in notas:
        cont += 1
        soma += n
    enotas['total'] = cont
    enotas['maior'] = max(notas)
    enotas['menor'] = min(notas)
    enotas['média'] = soma /cont
    if sit == True:
        if enotas['média'] >= 7:
            enotas['situação'] = 'Aprovado'
        elif enotas['média'] < 7 and enotas['media'] > 5:
            enotas['situação'] = 'Recuperação'
        else:
            enotas['situação'] = 'Reporvado'
    return enotas



resp = nota(5.5, 9.5, 10, 6.5, sit=True)
print(resp)