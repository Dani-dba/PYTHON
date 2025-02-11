from time import sleep
from pyton_6.pythonProject1.ex115.lib.arquivo import *
from pyton_6.pythonProject1.ex115.lib.interface import *

arq = 'cursoemvideo.txt'

if not ArquivoExiste(arq):
    CriarArquivo(arq)


while True:
    resposta = menu(['Ver Cadastros', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar conteúdos de um arquivo!
        LerArquivo(arq)
    elif resposta == 2:
        #opção de cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Sair do sistema
        cabeçalho('\033[35mSaindo do sistema... Até logo!\033[m')
        sleep(1)
        break
    else:
        print('\033[31mErro! digite uma opção válida!\033[m')
    sleep(2)
