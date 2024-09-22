numero = int(input('Digite um numero inteiro:'))
print('''Escolha uma opção de conversão:
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('o valor {} convertido em binario é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('O valor {} convertido em octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('O valor {} convertido em Hexadecimal é igual a {}'.format(numero,hex(numero)[2:]))
else:
    print('Opção inválida!')



