from textwrap import indent
from CadastroClientes.Interface import *
from time import sleep

def cadastrar_cliente(todosclientes, json):
    cabecalho('Cadastro de Cliente')
    cliente = {}
    while True:
        cliente['nome'] = str(input('Digite o nome do cliente: ')).upper().strip()
        if cliente['nome'] == '':
            print('\033[31mERRO! Digite um nome válido.\033[m')
        elif any(caractere.isnumeric() for caractere in cliente['nome']):
            print('\033[31mERRO! Não utilize números.\033[m')
        else:
            break
    while True:
        try:
            cliente['idade'] = int(input('Digite sua idade: '))
            break
        except(ValueError, TypeError):
            print('\033[31mDigite apenas números inteiros.\033[m')
    while True:
        try:
            cliente['telefone'] = int(input('Digite seu telefone: '))
            break
        except(ValueError, TypeError):
            print('\033[31mDigite apenas números inteiros.\033[m')
    print(f'Cliente {cliente["nome"]} cadastrado com sucesso.')
    todosclientes.append(cliente.copy())
    with open('clientes.json', 'w') as arquivo:
        json.dump(todosclientes, arquivo, indent=4)
    sleep(2)