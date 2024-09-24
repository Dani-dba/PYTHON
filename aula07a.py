n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1+n2
m = n1*n2
d = n1//n2
di = n1/n2
print('A soma é igual a {},\n a multiplicação é igual a {},\n a divisão é igual a {:.1f}'.format(s, m, d))
print('Divisão inteira igual a {:.1f}'.format(di))
