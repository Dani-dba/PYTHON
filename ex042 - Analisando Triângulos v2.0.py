r1 = int(input('Insira o primeiro segmento:'))
r2 = int(input('Insira o segundo segmento:'))
r3 = int(input('Insira o terceiro segmento:'))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Os segmentos podem formar um triangulo: ', end='')
    if r1 == r2 == r3:
        print('Equilatero!')
    elif r1!= r2 != r3 != r1:
        print ('Escaleno!')
    else:
        print('Isósceles!')
else:
    print ('Os segmentos não podem formar triângulo!')