# nome = str(input('Nome: '))
# média = float(input(f'Média de {nome}: '))
# situação = {'1': 'Aprovado', '0': 'Reprovado'}
# resultado = []
# if média <= 6:
#     resultado.append(situação['0'])
# else:
#     resultado.append(situação['1'])
#
# print(f'Nome é igual a {nome}')
# print(f'Média é igual a {média}')
# print(f'Situação é igual a {resultado[0]}')
aluno = {}
aluno['nome'] = str(input('Nome:'))
aluno['média'] = float(input(f'Média de {aluno["nome"]}:'))
if aluno['média'] > 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['média']:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')

