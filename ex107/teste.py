import moeda
preço = float(input('Digite o preço R$: '))
print(f'A metade do preço {preço} é igual a {moeda.metade(preço)}')
print(f'O dobro do preço {preço} é igual a {moeda.dobro(preço)}')
print(f'Com aumento de 10% o valor de {preço} sobe para {moeda.aumentar(preço, 10)}')
print(f'Com desconto de 10% o valor de {preço} sobe para {moeda.diminuir(preço, 10)}')