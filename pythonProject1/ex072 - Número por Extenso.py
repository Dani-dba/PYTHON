tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
# print(tupla)
n = int(input('Digite um numero de 0 a 20: '))
while n > 20:
    n = int(input('Numero inválido, digite um numero de 0 a 20: '))
print(tupla[n])