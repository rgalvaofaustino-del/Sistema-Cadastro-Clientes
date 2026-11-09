from CadastroClientes.Interface import *
from time import sleep

def excluir_cliente(todosclientes, json):
    cabecalho('Excluir Cliente')
    pessoa = input('Digite o cliente para excluir: ').upper()
    for cliente in todosclientes:
        if pessoa == cliente['nome']:
            todosclientes.remove(cliente)
            with open('clientes.json', 'w') as arquivo:
                json.dump(todosclientes, arquivo)
            print(f'Cliente {cliente['nome']} removido com sucesso.')
            break
    else:
        print('Não existe este cliente para remover.')
    sleep(2)