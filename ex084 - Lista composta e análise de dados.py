dado = []
pessoas = list()
mai = men = 0
while True:
    dado.append(str(input('Digite seu nome: ')))
    dado.append(float(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    continuar = (str(input('Deseja continuar? S/N: ')))
    while continuar not in 'sSNn':
        continuar = (str(input('Opção inválida, escolha S ou N: ')))
    if continuar in 'nN':
        break

# print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas')

print(f'O maior peso é {mai} kg, de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]} ', end= '')
print(f'\nO menor peso é {men} kg, de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]} ', end='')

