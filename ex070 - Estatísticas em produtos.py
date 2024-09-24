#produto = ''
barato = ''
total = contmil = menor = maior = contprod = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = (float(input('Digite o valor do produto R$: ')))
    continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    total += preço
    contprod +=1
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if preço > 1000:
        contmil += 1
    if contprod == 1 or preço < menor:
        menor = preço
        barato = produto
    if continua == 'N':
        break
print (f'{contmil} produtos custaram mais de 1.000 reais.')
print(f'Total da compra: RS{total}')
print(f'O produto {barato} é o mais barato da lista')