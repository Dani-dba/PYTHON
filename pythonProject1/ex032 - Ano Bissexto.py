ano = int(input('Qual ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO.'.format(ano))