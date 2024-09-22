'''co =float (input ('Comprimento do cateto oposto:'))
ca = float (input('Comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {.2f}'.format(hi))'''

'''import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = math.hypot(co,ca)
print('O comprimento da hipotenusa é igual a {:.2f}'.format(hi))'''

from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = hypot(ca,co)
print('O comprimento da hipotenusa é igual a {:.2f}'.format(hi))