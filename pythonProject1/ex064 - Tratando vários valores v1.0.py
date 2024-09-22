n = int(input('Digite um numero: '))
total = n
cont = 0
while n != 999:
    n = int(input('Digite um numero: '))
    cont += 1
    if n != 999:
        total += n
print('Foram digitados {} numeros e a soma entre eles é igual a: {} !'.format(cont, total))
