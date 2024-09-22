a = float(input('Insira a altura:'))
L = float(input('insira a largura:'))
ar = a*L
qtd = ar / 2
print('Sua parede tem a dimensão de {} x {} e sua area é {}'.format(L, a, ar))
print('A quantidade necessaria de tinta para pintar a area calculada é de {:.2f} litros'.format(qtd))