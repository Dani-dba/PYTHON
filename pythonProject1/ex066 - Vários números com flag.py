n = 0
contador = 0
soma = 0
while True:
    n = int(input('Digite um numero inteiro: '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'Você digitou {contador} numeros, a soma entre eles é igual a {soma}')