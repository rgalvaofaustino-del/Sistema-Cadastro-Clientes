from CadastroClientes.Interface import *
from time import sleep

def buscar_cliente(todosclientes):
    cabecalho('Buscar Clientes')
    pessoa = input('Digite o nome do cliente:').upper()
    tem = False
    for cliente in todosclientes:
        if pessoa == cliente['nome']:
            tem = True
            print('Cliente Encontrado.')
            for k, v in cliente.items():
                print(f'{k} : {v}')
    if tem == False:
        print('Cliente não encontrado.')
    sleep(2)