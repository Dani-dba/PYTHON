#numero = int(input('Digite o numero para calcular o fatorial: '))
n = int(input('Digite o numero para calcular o fatorial: '))
contador = n
fatorial = 1
print('O calculo fatorial de {}! é: '.format(n),end='')
for c in range(n, 0, -1):
    print(c, end='')
    print('x' if c > 1 else '=', end='')
    fatorial *= c
    c -= 1
print('{}'.format(fatorial), end='')



'''numero = int(input('Digite um numero para calculo de fatorial:'))
contador = numero
fatorial = 1
print('Calculando {}! = '.format(numero), end='')
while contador > 0:
    print('{}'. format(contador), end='')
    print('x' if contador > 1 else '=', end='')
    fatorial *= contador
    contador -= 1
print(' {}'.format(fatorial), end='')'''

'''from math import factorial
numero = int(input('Digite um numero para calculo de fatorial:'))
fatorial = factorial(numero)
print('O fatorial de {} é: {}'.format(numero, fatorial))'''

'''numero = int(input('Digite um numero para calculo de fatorial:'))
contador = 1
resultado = 1
while contador <= numero:
    resultado *= contador
    contador += 1
print('O resultado fatorial do numero escolhido é igual a {}'.format(resultado))'''