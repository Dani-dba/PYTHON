from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')
computador = randint(0,4)
#print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
[0] \033[35mPedra\U0001FAA8\033[m
[1] \033[35mPapel\U0001F4C4\033[m
[2] \033[35mTesoura\U00002702\033[m
[3] \033[35mLagarto\U0001F98E\033[m
[4] \033[35mSpock\U0001F596\033[m
''')
print('-='*10)
jogador = int(input('Qual sua Jogada? '))
print('-='*10)
print ('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-='*10)
print('Você escolheu {}'.format(itens[jogador]))
print('Computador escolheu {}'.format(itens[computador]))
if computador == 0:  #pedra
    if jogador == 0: #pedra
        print('EMPATE')
    elif jogador == 1: #papel
        print ('Papel cobre pedra!')
        print('\033[32mVOCÊ VENCEU!\U0001F604\033[m')
    elif jogador == 2: #tesoura
        print('Pedra quebra tesoura!')
        print('\033[31mVOCÊ PERDEU!\U0001F614\033[m')
    elif jogador == 3: #Lagarto
        print('Pedra esmaga Lagarto!')
        print('\033[31mVOCÊ PERDEU!\U0001F614\033[m')
    elif jogador == 4: #spock
        print('Spock vaporiza pedra!')
        print('\033[32mVOCÊ VENCEU!\U0001F604\033[m')
elif computador == 1: #PAPEL
    if jogador == 0: #PEDRA
       print('Papel cobre pedra!')
       print('\033[31mVOCÊ PERDEU!\U0001F614\033[m')
    elif jogador == 1: #PAPEL
        print('\033[33mEMPATE!\033[m')
    elif jogador == 2: #TESOURA
        print('Tesoura corta papel')
        print('\033[32mVOCÊ VENCEU!\U0001F604\033[m')
    elif jogador == 3: #Lagarto
        print('Lagarto come papel!')
        print('\033[32mVOCÊ VENCEU!\U0001F604\033[m')
    elif jogador == 4: #SPOCK
        print('Papel refuta Spock')
        print('\033[31mVOCÊ PERDEU!\U0001F614\033[m')
elif computador == 2: #TESOURA
    if  jogador == 0: #PEDRA
        print('Pedra quebra Tesoura!')
        print('\033[32mVOCÊ VENCEU!\U0001F604\033[m')
    elif jogador == 1: #PAPEL
        print('Tesoura corta Papel!')
        print('\033[31mVOCÊ PERDEU!\U0001F614\033[m')
    elif jogador == 2: #TESOURA
        print('EMPATE')
    elif jogador == 3:#Lagarto
        print('Tesoura decapita Lagarto!')
        print('\033[31mVOCÊ PERDEU!\U0001F614\033[m')
    elif jogador == 4:#SPOCK
        print('Spock derrete Tesoura!')
        print('\033[32mVOCÊ VENCEU!\U0001F604\033[m')
elif computador == 3: #Lagarto
    if jogador == 0: #PEDRA
        print('Pedra esmaga Lagarto!')
        print('\033[32mVOCÊ VENCEU!\U0001F604\033[m')
    elif jogador == 1: #PAPEL
        print('Lagarto come papel!')
        print('\033[31mVOCÊ PERDEU!\U0001F614\033[m')
    elif jogador == 2: #TESOURA
        print('Tesoura decapita Lagarto!')
        print('\033[32mVOCÊ VENCEU!\U0001F604\033[m')
    elif jogador == 3: #Lagarto
        print('\033[33mEMPATE!\033[m')
    elif jogador == 4: #SPOCK
        print('Lagarto envenena Spock!')
        print('\033[31mVOCÊ PERDEU!\U0001F614\033[m')
elif computador == 4: #SPOCK
    if jogador == 0: #PEDRA
        print('Spock vaporiza Pedra!')
        print('\033[31mVOCÊ PERDEU!\U0001F614\033[m')
    elif jogador == 1: #PAPEL
        print('Papel refuta Spock!')
        print('\033[32mVOCÊ VENCEU!\U0001F604\033[m')
    elif jogador == 2: #TESOURA
        print('Spock derrete Tesoura!')
        print('\033[31mVOCÊ PERDEU!\U0001F614\033[m')
    elif jogador == 3: #Lagarto
        print('Lagarto envenena Spock!')
        print('\033[32mVOCÊ VENCEU!\U0001F604\033[m')
    elif jogador == 4: #SPOCK
        print('\033[33mEMPATE!\033[m')