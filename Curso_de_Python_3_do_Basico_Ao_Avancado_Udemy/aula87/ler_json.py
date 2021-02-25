import json

with open('aula87\\abc.json', 'r') as file:
    d1_json = file.read()
    print(d1_json)
    d1 = json.loads(d1_json)
    print(d1)