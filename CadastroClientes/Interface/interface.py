def menu(lista):
    c = 1
    cabecalho('SISTEMA DE CLIENTES')
    for linha in lista:
        print(f'{c} - {linha}')
        c += 1
    lin()

def cabecalho(msg):
    print('-'*42)
    print(msg.center(42))
    print('-'*42)

def lin():
    print('-'*42)