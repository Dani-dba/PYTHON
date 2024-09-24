pessoas = {'Nome': 'Danielle', 'Idade': '31', 'Sexo': 'F'}
# print(pessoas.keys()) #exibe as chaves ou variaveis compostas
# print(pessoas.values()) #exibe os dados das tuplas
# print(pessoas.items())#exibe o dicionario e os dados
# for k in pessoas:
#     print(f'{k}')
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(estado1)
print(estado2)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['uf'])
estado = dict()
brasil = list()
for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #para copiar os dados inseridos em sigla e uf dentro da lista brasil
print(brasil)
for e in brasil: #mostra uf e sigla com a formatação
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for e in brasil: #mostra uf e sigla sem formatação.
    for v in e.values():
        print(v, end=' ')
    print()