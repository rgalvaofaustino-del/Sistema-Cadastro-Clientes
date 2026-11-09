from Funções import *
from Interface import *
from time import sleep
import json

cliente = {}
opc = 0

try:
    with open('Clientes.json', 'r') as arquivo:
        todosclientes = json.load(arquivo)
except FileNotFoundError:
    todosclientes = []

while opc != 5:
    menu(['Cadastrar Clientes', 'Listar Clientes', 'Buscar Clientes', 'Excluir Clientes', 'Sair'])

    while True:
        try:
            opc = int(input('Sua opção: '))
        except:
            print('\033[31mERRO! Digite uma opção válida.\033[m')
            continue
        if opc > 5 or opc <= 0:
            print('\033[31mERRO! Digite uma opção válida.\033[m')
        else:
            break
    lin()
    sleep(2)


    if opc == 1:
       cadastrar_cliente(todosclientes, json)

    if opc == 2:
        listar_clientes(todosclientes)

    if opc == 3:
        buscar_cliente(todosclientes)

    if opc == 4:
        excluir_cliente(todosclientes, json)

    if opc == 5:
        cabecalho('Finalizando...')
        sleep(2)
