import json


d1 = {
    'Pessoa1': {
        'nome': 'Danilo',
        'idade': 27
    },
    'Pessoa2': {
        'nome': 'Maria',
        'idade': 28
    }
}

d1_json = json.dumps(d1)

with open('aula87\\abc.json', 'w+') as file:
    file.write(d1_json)
