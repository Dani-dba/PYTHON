'''print ('Sequencia de Fibonacci:')
print('-='*50)
n = int(input('Quantos numeros você deseja ver? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('\n''fim')'''
n = int(input('Quantos termos deseja ver? '))
t1 = 0
t2 = 1
contador = 1
print('{} -> '.format(t1), end='')
print('{} -> '.format(t2), end='')
while contador <= n:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print('Fim')

