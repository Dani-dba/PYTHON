preco = float(input('Digite o valor da compra:'))
condicao = int(input(''' ESCOLHA A OPÇÃO DE PAGAMENTO:
[1] DINHEIRO/ PIX
[2] Cartão à vista
[3] em 2x no cartão
[4] 3x ou mais
Qual será a forma de pagamento?
'''))
if condicao == 1:
    total = preco - (preco * 10 /100)
elif condicao == 2:
    total = preco - (preco * 5/100)
elif condicao == 3:
    total = preco
elif condicao == 4:
    parcela = int(input('Em quantas parcelas:'))
    total = preco + (preco * 20/100)
    totalfinal = total / parcela
    print('O valor total da sua compra será de R${:.2f} em {:.0f} vezes de {:.2f}'.format(total, parcela, totalfinal))
else:
    total = preco
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE')

print('O total da sua compra será de R${:.2F}'.format(total))

'''vista = 10
cartao = 5
duas = 0
tres = 20
desc10 = preco * (vista / 100)
desc5 = preco * (cartao / 100)
juro20 = preco * (tres / 100)
condicao = str(input('Digite a condição de pagamento: '))
if condicao == 'dinheiro' or condicao == 'cheque':
    print (preco - desc10)
elif condicao == 'cartão a vista':
    print(preco-desc5)
elif condicao == 'em 3x':
    print(preco + juro20)
else:
    print(preco)'''
