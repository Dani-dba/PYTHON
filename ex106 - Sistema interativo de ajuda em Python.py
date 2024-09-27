from time import sleep
c = ('\033[m', #sem cor
    '\033[0;30;41m', #vermelho
    '\033[0;30;42m', #verde
    '\033[0;30;43m', #amarelo
    '\033[0;30;44m', #azul
    '\033[0;30;45m', #roxo
    '\033[47m', #Branco
);


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título (msg, cor=0):
    print(c[cor], end='')
    tam = len(msg) + 4
    print('~'* tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#Programa Principal
comando = ''
while True:
    título('Sistema de ajuda PyHelp', 2)
    comando = str(input('Função ou biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até Logo!',1)