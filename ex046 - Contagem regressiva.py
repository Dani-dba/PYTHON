#Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

'''from time import sleep
print('Contagem Regressiva:')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Feliz ano novo')'''

from time import sleep
i = 11
p = 1
f = 0
print('Contagem regressiva:')
for c in range(i-1, f, -1):
    print(c)
    sleep(p)
print('\033[33mFeliz Ano novo!\033[0m')
print('\U0001F386'*10)

