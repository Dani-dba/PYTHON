from random import randint
computador= randint(0,5) #faz o computador pensar
'''print('pensei no numero...{}'.format(computador))'''
print('Vou pensar em um numero entre 0 e 5, tente adivinhar:')
print('-=-'*10)
jogador= int(input('Em que numero eu pensei?'))
print('-=-'*10)
print('Parabéns, você acertou *-*!' if jogador == computador else 'Você errou :(!')