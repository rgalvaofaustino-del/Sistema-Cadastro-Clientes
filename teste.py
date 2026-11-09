import json

clientes = [
    {'nome': 'Joao', 'idade': 25, 'telefone': '1199999999'},
    {'nome': 'Renato', 'idade': 18, 'telefone': '11989929788'}
]

with open('CadastroClientes/clientes.json', 'w') as arquivo:
    json.dump(clientes, arquivo)

clientes_salvos = []

with open('CadastroClientes/clientes.json', 'r') as arquivo:
    clientes_salvos = json.load(arquivo)
print(clientes_salvos)