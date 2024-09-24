frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a primeira vez que a letra aparece é na posiçao {}'.format(frase.find('A')+1))
print('A ultima vez que aparece é na posição {}'.format(frase.rfind('A')+1))