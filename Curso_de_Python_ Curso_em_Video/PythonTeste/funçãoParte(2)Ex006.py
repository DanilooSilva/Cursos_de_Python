def pyHelp(comando):
    from time import sleep
    def formataTexto(mgn, corTexto=37, corFunto=48):
        tm = len(mgn) + 4
        print('\033['+str(corTexto)+';'+str(corFunto)+'m'+'~' * tm)
        print(f'  {mgn}', flush=False)
        print('~' * tm)
        print('\033[m')
    while True:
        formataTexto('Sistema de Ajuda PyHelp', 32, 46)
        cm = str(input(comando))
        print()
        if cm.upper() == 'FIM':
            formataTexto('Até Logo!', corFunto=41)
            break
        formataTexto(f'Acessando o manual do comando  \'{cm}\'', 36, 42)
        sleep(3)
        print('\033[7;30m', end='')
        help(cm)
        print('\033[m')


pyHelp('Função ou Biblioteca: ')


