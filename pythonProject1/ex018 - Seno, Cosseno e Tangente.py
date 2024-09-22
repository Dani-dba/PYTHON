'''import math
ângulo = float(input('Digite o angulo que você deseja:'))
seno = math.sin(math.radians(ângulo))
print('O angulo de {:.0f} tem o seno de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O angulo de {:.0f} tem o cosseno de {:.2f}'.format(ângulo,cosseno))
tangente = math.tan(math.radians(ângulo))
print('O angulo de {:.0f} tem a tangente de {:.2f}'.format(ângulo,tangente))'''


from math import radians, sin, cos, tan
angulo = float (input('Digite o angulo que você deseja'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo {:.0f} tem o seno {:.2f}'.format(angulo, seno))
print('O angulo {:.0f} tem o cosseno {:.2f}'.format(angulo, cosseno))
print('O angulo {:.0f} tem a tanngente {:.2f}'.format(angulo, tangente))


