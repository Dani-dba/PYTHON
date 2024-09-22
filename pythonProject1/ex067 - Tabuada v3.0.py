from time import sleep
n = 1
while True:
    n = int(input('Digite um numero para ver sua tabuada: '))
    if n < 0:
        print('Finalizando Tabuada...')
        sleep(2)
        print('Tabuada finalizada!')
        break

    print('-'*30)
    for c in range(1,11):
        print (f'{n} x {c} = {c*n}')
    print('-'*30)
