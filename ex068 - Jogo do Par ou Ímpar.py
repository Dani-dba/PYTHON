from time import sleep
from random import randint
print('-' *30)
print('Vamos jogar par ou impar!')
user = 0
par_impar = ''
#print(f'{computador}')
contador_w = 0
contador_l = 0
computador = randint(1, 10)
resultado = computador + user
while True:
    user = int(input('Me diga um numero: '))
    par_impar = str(input('Par ou impar? [P/I]')).upper()
    resultado = computador + user
    while par_impar not in 'PI':
        par_impar = str(input('Par ou impar? [P/I]')).upper()[0]
    print(f'Você jogou {user} e o computador {computador}, total de {resultado}')
    if par_impar == 'P':
        if resultado % 2 == 0:
            print('Você venceu! ')
            contador_w += 1
        else:
            print('Você perdeu!\U0001F622')
            break
    elif par_impar == 'I':
        if resultado % 2 == 1:
            print('Impar, você venceu!')
            contador_w += 1
        else:
            contador_l += 1
            print(f'Impar, você perdeu:\U0001F622')
            break
sleep(2)
print('Calculando resultados...')
sleep (2)
print(f'Você venceu {contador_w} vezes. Parabéns! 🎉')
sleep(2)
print('Finalizando jogo...')
sleep(2)
print('Jogo finalizado!')