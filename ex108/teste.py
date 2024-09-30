import moeda
preço = float(input('Digite o preço R$: '))
print(f'A metade do preço {moeda.moeda(preço)} é igual a {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro do preço {moeda.moeda(preço)} é igual a {moeda.moeda(moeda.dobro(preço))}')
print(f'Com aumento de 10% o valor de {moeda.moeda(preço)} sobe para {moeda.moeda(moeda.aumentar(preço, 10))}')
print(f'Com desconto de 10% o valor de {moeda.moeda(preço)} sobe para {moeda.moeda(moeda.diminuir(preço, 10))}')