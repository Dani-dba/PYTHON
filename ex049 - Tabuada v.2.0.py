num = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1,11):
    print('{} x {:2} = {}'.format(num, c, num*c))
