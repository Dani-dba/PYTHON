def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite uma opção válida.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mO usuário interrompeu o programa..\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc