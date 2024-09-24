from random import randint
computador = randint(0,10)
contador = 0 #palpite
print('-'*10,'='*10,'-'*10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
print('-='*30)
user = ''
while user != computador:
    user = int(input('Qual é o seu palpite? '))
    contador += 1 #palpite
    if computador < user:
        print('Menos... tente mais uma vez!')
    elif computador > user:
        print('Mais... Tente novamente!')
    else:
        print('Você acertou, mas você precisou de {} tentativas.'.format(contador))
'''if user == computador:
    print('Você acertou, mas você precisou de {} tentativas.'.format(contador))'''