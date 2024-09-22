from random import randint
from time import sleep
lista = []
jogos = []
print(' - =' * 20)
print('     MEGA SENA     ')
print(' - = ' * 20)
qtd = int (input('Quantos jogos serão criados? '))

# for p in range(qtd):
#     palpite = ([randint(1,60)], [randint(1,60)], [randint(1,60)], [randint(1,60)], [randint(1,60)], [randint(1,60)])
#     print(palpite)
tot = 1
while tot <= qtd:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {qtd} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}:{l}')
    sleep(1)
print('-=' * 5, '<BOA SORTE!>', '-=' * 5)
