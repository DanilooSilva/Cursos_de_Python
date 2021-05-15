from encontra_arquivos import EncontraArquivos


caminho_procura = str(input('Digite o caminho do diretorio.:  '))
termo_procura = str(input('Digite o arquivo que deseja procurar.:  '))

pr = EncontraArquivos(caminho=caminho_procura, arquivo=termo_procura)
