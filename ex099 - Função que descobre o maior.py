

from time import sleep


def lin():
    print('-' * 40)


def maior(*num):
    cont = maior = 0
    lin()
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ',end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'\nForam informados {cont} valores ao todo.')
    lin()
    sleep(1)
    print(f'O maior valor informado foi o número {maior}.')
    lin()

#Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(2, 8, 9)
maior(1, 9)
maior(6)
maior()