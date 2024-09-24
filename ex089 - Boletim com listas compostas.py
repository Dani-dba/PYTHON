from time import sleep
ficha = list()
cont = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = (str(input('Quer continuar? S/N:')))
    # if resp in 'Ss':
    #     cont +=1
    while resp not in 'SsNn':
        resp = (str(input('Resposta invalida, por favor escolha S ou N: ')))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? (999 para interromper análise)'))
    if opc == 999:
        sleep(1)
        print('FINALIZANDO..')
        break
    if opc <= len(ficha) -1:
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}')
sleep(1)
print('<<< VOLTE SEMPRE!')