import moeda
preço = float(input('Digite o preço R$: '))
print(f'A metade do preço {moeda.moeda(preço)} é igual a {moeda.metade(preço, True)}')
print(f'O dobro do preço {moeda.moeda(preço)} é igual a {moeda.dobro(preço, True)}')
print(f'Com 10% de juros o valor será {moeda.aumentar(preço, 10, True)}')
print(f'Com 10% de desconto o valor será {moeda.diminuir(preço, 10, True)}')
print(f'Com 13% de desconto o valor será {moeda.diminuir(preço, 13, True)}')

