def lin():
    print('-' * 30)

def area (larg, comp):
    a = largura*comprimento
    print(f'A area de um terreno {larg}x{comp} é de {a}m²')

lin()
print('CONTROLE DE TERRENOS')
lin()
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura, comprimento)


