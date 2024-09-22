preco_original = float(input('Insira o preço original do produto:'))
percentual_desconto = float(input('Qual o percentual de desconto:'))
fator_desconto = percentual_desconto / 100
valor_com_desconto = preco_original * (1 - fator_desconto)
print('O valor do produto com {} de desconto é {:.0f}'.format(percentual_desconto, valor_com_desconto))
