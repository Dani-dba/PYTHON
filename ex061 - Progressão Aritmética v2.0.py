primeiro_termo = int(input('Digite o primeiro termo da PA:'))
razão = int(input('Digite a razão da PA:'))
cont = 1
termo = primeiro_termo
while cont <= 10:
    termo = termo + razão
    cont = cont + 1
    print('{} - '.format(termo), end='')
print('\n''fim')