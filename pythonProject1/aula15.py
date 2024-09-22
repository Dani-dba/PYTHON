

'''cont = 1
while cont <= 10:
    print (cont, ' ', end='')
    cont += 1
print('Acabou')
'''
'''cont' = 1
while true:
    print (cont, ' ', end='')
    cont += 1
print('Acabou') ''' #cria um loop infinito
'''n = 0
while n != 999:
    n = int(input('Digite um numero: '))''' #lê numeros até incluir a flag de parada
'''n = 0
contador = 0
while contador < 3:
    n = int(input('Digite um numero: '))
    contador += 1'''# lê numeros até chegar no numero maximo definido pelo contador.
'''n = s = 0
while n != 999:
    n = int(input('Digite um numero: '))
    s += n
s -= 999
print('A soma é igual a {}'.format(s))'''#gambiarra pra não contar o 999 na soma geral
'''n = s = 0
while True:
    n = int(input('Digite um numero:'))
    s += n''' #solicita numeros infinitamente
'''n = s = 0
while True:
    n = int(input('Digite um numero:'))
    if n == 999:
        break
    s += n
print('A soma é igual a {}.'.format(s))''' #inlcui uma condição de parada sem somar a flag no final
'''n = s = 0 
while True:
    n = int(input('Digite um numero:'))
    s += n
    if n == 999:
        break
print('A soma é igual a {}.'.format(s))''' #exemplo de que o break tem que estar antes da variavel somatória.
'''n = s = 0
while True:
    n = int(input('Digite um numero:'))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')'''#usando fstring no print.
'''nome = 'José'
idade = '33'
print (f'{nome} tem {idade} anos.') #fstring
print('{} tem {} anos.'.format(nome, idade)) #forma anterior
print('%s tem %s anos' % (nome, idade)) #python2
#modo de interpulação
print(f'{nome:^10} tem {idade}') #centraliza o nome entre os 10 espaços a mais que incluí.
print(f'{nome:-^10} tem {idade}') #centraliza o nome e os traços nos 10 espaços a mais
print(f'{nome:->10} tem {idade}')#alinha o nome à direita dos traços nos 10 espaços a mais.
print(f'{nome:-<10} tem {idade}')#alinha o nome à esquerda dos traços nos 10 espaços a mais.'''
