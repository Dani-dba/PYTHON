num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print ('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel \033[33m{}\033[m vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele \033[34mÉ PRIMO!\033[m')
else:
    print('E por isso ele \033[31mNÃO É PRIMO\033[m')