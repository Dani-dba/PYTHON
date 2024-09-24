lista1 = []
listap = []
listai = []
while True:
    n = int(input('Digite um valor: '))
    lista1.append(n)
    if n % 2 == 0:
        listap.append(n)
    elif n % 2 == 1:
        listai.append(n)
    r = str(input('Deseja continuar? [S/N]:'))
    if r in 'Nn':
        break
print('-='*30)
print(f'Você digitou os valores {lista1}')
print(f'Sendo os valores {listap} pares')
print(f'E os valores {listai} ímpares')