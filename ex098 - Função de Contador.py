from time import sleep

def contador (i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(1)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(1)
            cont -= p
        print('Fim!')

#programa principal
contador (0, 10, 1)
contador(10, 0, 2)
contador(i= int(input('Digite o valor inicial:')),
         f= int(input('Digite o valor final: ')),
         p= int(input('Digite o passo: ')))