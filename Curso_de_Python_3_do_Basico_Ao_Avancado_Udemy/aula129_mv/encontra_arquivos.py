import os


class EncontraArquivos:
    def __init__(self, arquivo, caminho='C:\\Users\\Danilo Gomes\\Desktop'):
        self.arquivo = arquivo
        self.caminho = caminho
        self.encontra()

    @property
    def arquivo(self):
        return self._arquivo

    @property
    def caminho(self):
        return self._caminho

    @arquivo.setter
    def arquivo(self, arq):
        self._arquivo = arq

    @caminho.setter
    def caminho(self, cmh):
        self._caminho = cmh

    def encontra(self, cmnh=None, arq=None):
        if cmnh != None and arq != None:
            self.__caminho_aux = cmnh
            self.__arquivo_aux = arq
        else:
            self.__caminho_aux = self._caminho
            self.__arquivo_aux = self._arquivo
        self.__conta = 0
        for raiz, diretorios, arquivos in os.walk(self.__caminho_aux):
            for arquivo in arquivos:
                try:
                    if self.__arquivo_aux in arquivo:
                        self.__conta += 1
                        self.__caminho_completo = os.path.join(raiz, arquivo)
                        self.__nome_arquivo, self.__ext_aquivo = os.path.splitext(arquivo)
                        self.__tamanho = os.path.getsize(self.__caminho_completo)
                        
                        print()
                        print('Encontrei o arquivo: ', arquivo)
                        print('Caminho: ', self.__caminho_completo)
                        print('Nome: ', self.__nome_arquivo)
                        print('Extensão: ', self.__ext_aquivo)
                        print('Tamanho: ', self.formata_tamanho(self.__tamanho))
                except PermissionError as e:
                    print('Sem permissão')
                except FileNotFoundError as e:
                    print('Arquivo não encontrado.')
                except Exception as e:
                    print('Erro desconhecido. ', e)
        print()
        print(f'{self.__conta} arquivo(s) encontrado(s)')

    @staticmethod
    def formata_tamanho(tmh):
        base = 1024
        kilo = base
        mega = base ** 2
        giga = base ** 3
        tera = base ** 4
        peta = base ** 5

        if tmh < kilo:
            texto = 'B'
        elif tmh < mega:
            tmh /= kilo
            texto = 'k'
        elif tmh < giga:
            tmh /= mega
            texto = 'M'
        elif tmh < tera:
            tmh /= giga
            texto = 'G'
        elif tmh < peta:
            tmh /= tera
            texto = 'T'
        else:
            tmh /= peta
            texto = 'P'

        tmh = round(tmh, 2)
        return f'{tmh}{texto}'
