pt = int(input('Primeiro Termo:'))
rz = int(input('Razão:'))
dcm = pt + (10 - 1) * rz
for c in range(pt, dcm + rz, rz):
    print('{}'.format(c), end=' ')
