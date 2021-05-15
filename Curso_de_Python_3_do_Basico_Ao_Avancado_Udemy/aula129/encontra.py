import os

caminho_procura = 'C:\\Users\\Danilo Gomes\\Desktop'
termo_procura = 'faketable'

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'k'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'

conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        try:
            if termo_procura in arquivo:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_aquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                
                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', ext_aquivo)
                print('Tamanho: ', formata_tamanho(tamanho))
        except PermissionError as e:
            print('Sem permissão')
        except FileNotFoundError as e:
            print('Arquivo não encontrado.')
        except Exception as e:
            print('Erro desconhecido. ', e)

print()
print(f'{conta} arquivo(s) encontrado(s)')