from pyton_6.pythonProject1.ex115.lib.interface import *

def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro ao criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def LerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('Pessoas Cadastradas')
        # print(a.read())
        print(f"{'Nome:':<30}{' Idade:'}")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos ')
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade='0'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve erro ao gravar o dado.')
        else:
            print(f'Novo registro de {nome} adicionado.')
