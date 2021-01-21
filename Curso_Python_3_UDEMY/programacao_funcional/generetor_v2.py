#! python3
from programacao_funcional.generetor_v1 import cores_arco_ires

if __name__ == '__main__':
    generetor = cores_arco_ires()
    for cor in generetor:
        print(cor)
    print('Fim')
