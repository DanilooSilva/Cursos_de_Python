import PyPDF2
import os

caminho_dos_pdf = r'E:\Danilo Gomes\Documents\GitHub\Cursos_de_Python\Curso_de_Python_3_do_Basico_Ao_Avancado_Udemy\aula144'

"""
novo_pdf = PyPDF2.PdfFileMerger()

for root, dirs, files in os.walk(caminho_dos_pdf):
    for file in files:
        if '.pdf' in file:
            caminho_completo_arquivo = os.path.join(root, file)
            
            arquivo_pdf = open(caminho_completo_arquivo, 'rb')
            novo_pdf.append(arquivo_pdf)


with open(fr'{caminho_dos_pdf}\novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)
"""
with open(fr'{caminho_dos_pdf}\novo_arquivo.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()
    
    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(fr'{caminho_dos_pdf}\{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)