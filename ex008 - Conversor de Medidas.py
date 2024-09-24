n1 = float(input('Insira a quantidade de metros:'))
km = n1/1000
hm = n1 / 100
dam = n1 /10
dm = n1 *10
cm = n1 * 100
mm = n1 * 1000
print('Resultado dos valores em:'
      '\n quilometro {}'
      '\n hectometro {}'
      '\n decametro é {}'
      '\n decimetro {:.0f}'
      '\n centímetros é {:.0f}'
      '\n milimetros é {:.0f}.'.format(km, hm, dam, dm, cm, mm))
