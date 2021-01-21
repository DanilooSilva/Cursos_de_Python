with open('desafio-ibge.csv', encoding='ISO-8859-1') as arquivo:
    for inf in arquivo:
        inf = inf.strip().split(',')
        print(inf[8], inf[3])