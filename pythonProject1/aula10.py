#Condições
'''tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro Novo!')
else:
    print('Carro velho!')
print('--Fim--')'''


'''nome = str(input('Digite seu nome:'))
if nome == 'Danielle':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print('Bom dia, {}'.format(nome))'''

n1= float(input('Digite a primeira nota:'))
n2= float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
'''print('A sua média foi {:.2f}'.format(m))
if m >=6:
    print('Parabéns, você foi aprovado!')
else:
    print('Sinto muito, você foi reprovado!')'''
print('Parabéns, você foi aprovado!' if m >= 6 else 'Sinto muito, você foi reprovado!')

