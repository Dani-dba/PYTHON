nome = str(input ('Qual é o seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Danielle' or nome == 'Advaldo' or nome == 'Ygor':
    print ('Seu nome é bem popular no Brasil!')

elif nome in 'Ana Cláudia Juliana':
    print('Belo nome feminino!')
'''else:
    print('Seu nome é bem normal.')'''
print('Tenha um bom dia {}!'.format(nome))

