from time import sleep
primeiro = int(input('Digite o primeiro termo: '))
razão= int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos deseja visualizar? '))

print('Finalizando progressão...')
sleep(2)
print('Progressão finalizada! Foram exibidos {} termos.'.format(total))


