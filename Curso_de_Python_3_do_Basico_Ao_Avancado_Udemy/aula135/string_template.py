from string import Template
from datetime import datetime

with open(r'aula135\template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_mgn = template.substitute(nome="Danilo Gomes", data=data_atual)

print(corpo_mgn)