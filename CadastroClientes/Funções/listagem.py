from CadastroClientes.Interface import *
from time import sleep

def listar_clientes(todosclientes):
    cabecalho('Listar Clientes')
    c = 1
    for cliente in todosclientes:
        print(f'Cliente {c}')
        for k, v in cliente.items():
            print(f'{k} : {v}')
        print()
        c += 1
    sleep(2)