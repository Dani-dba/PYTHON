cadastro = dict()
cadastro['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
gols = []
for p in range(partidas):
    gols.append (int(input(f'Quantos gols na partida {p}? ')))
cadastro['gols'] = gols
cadastro['total'] = sum(gols)
print ('-=' *30)
print(cadastro)
print('-=' *30)
for k, v in cadastro.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {cadastro["nome"]} jogou {len(cadastro["gols"])} partidas. ')
for i, v in enumerate(cadastro['gols']):
    print(f'  => na partda {i}, fez {v} gols.')
print(f'Foi um total de {cadastro["total"]} gols.')
