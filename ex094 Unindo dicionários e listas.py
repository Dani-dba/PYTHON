galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if resp == 'N':
        break
media = soma / len(galera)
print('-=' *30)
print(f'A) Ao todo foram cadastradas {len(galera)} pessoas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f' {p["Nome"]},', end='')
print(f'\nD) Lista das pessoas com idade acima da média:')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()

print('<<< ENCERRADO!')


