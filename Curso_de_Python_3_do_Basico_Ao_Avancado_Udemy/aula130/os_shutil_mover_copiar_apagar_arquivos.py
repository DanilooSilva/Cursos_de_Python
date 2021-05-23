import os
import shutil

caminho_origem = r"E:\Danilo Gomes\Documents\GitHub\Cursos_de_Python\Curso_de_Python_3_do_Basico_Ao_Avancado_Udemy\aula130\Origem"
caminho_destino = r"E:\Danilo Gomes\Documents\GitHub\Cursos_de_Python\Curso_de_Python_3_do_Basico_Ao_Avancado_Udemy\aula130\Destino"

try:
    os.mkdir(caminho_destino)
except FileExistsError as e:
    print(f'Pasta {caminho_destino} já existe.')

for root, dirs, files in os.walk(caminho_origem):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_destino, file)
        
        # shutil.copy(old_file_path, new_file_path)
        # shutil.remove(new_file_path)
        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {file} movido com sucesso!')