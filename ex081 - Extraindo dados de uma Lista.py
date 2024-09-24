lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Deseja continuar? [S/N]:'))
    while r not in 'NnSs':
        r = str(input('Opção invalida, por favor, tente novamente: [S/N]: '))
    if r in 'Nn':
        break
print(f'Foram digitados {len(lista)} números.')
# print(f'Os numeros em ordem reversa são: {lista[::-1]}')
lista.sort(reverse=True)
print(f'Os numeros em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O numero 5 foi digitado e está na lista!')
else:
    print(f'Numero 5 não encontrado e não incluso na lista.')


