from zipfile import ZipFile
import os


caminho = r'E:\Danilo Gomes\Pictures'

with ZipFile(r'aula137\arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        #print(arquivo)
        if 'PNG' in arquivo or '.jpg' in arquivo:
            caminho_completo = os.path.join(caminho, arquivo)
            zip.write(caminho_completo, arquivo)

with ZipFile(r'aula137\arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

with ZipFile(r'aula137\arquivo.zip', 'r') as zip:
    zip.extractall(r'aula137\descompactado')