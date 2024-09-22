tupla = (int(input('Digite um valor:'))
         ,int(input('Digite um valor:'))
         ,int(input('Digite um valor:'))
         ,int(input('Digite um valor:')))
print (f'Você digitou os valores {tupla}')
print(f'O numero 9 apareceu {tupla.count(9)} vezes.')
print(f'O primeiro numero 3 apareceu na posição {tupla.index(3)+1}')
for c in tupla:
    if c % 2 == 0:
        print(f'O numero {c} é par')



