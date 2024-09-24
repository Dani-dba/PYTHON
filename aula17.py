# num = (2, 5, 9, 1)
# #tuplas são imutáveis
# num [2] = 3 #TypeError: 'tuple' object does not support item assignment
# print (num)
#listas são mutáveis
num = [2, 5, 9, 1]
print(f'Ordem inicial dos numeros {num}')
num [2] = 3 #altera o item 2 da lista de 9 para 3
print (f'altera o item 2 da lista de 9 para 3: {num}') #[2, 5, 3, 1]
# num[4] = 7 #IndexError: list assignment index out of range, comando invalido para inclusão em listas.
num.append(7) #inclui mais um item na lista
print (f'inclui mais um item na lista{num}') #[2, 5, 9, 1, 7]
num.sort() #mostra em ordem numerica ou alfabética
print(f'em ordem numerica {num}') #[1, 2, 5, 7, 9]
num.sort(reverse=True) #mostra em ordem reversa, numerica ou alfabética.
print(f'em ordem reversa {num}') #[9, 7, 5, 2, 1]
print(f'Essa lista tem {len(num)} elementos.') #mostra a quantidade de itens que estão na lista.
#todas as alterações não são definitivas, devendo-se manter o comando para exibir todas elas.
num.insert(2,0)#inclui o numero 0 depois do num 3 aumentando os valores da lista
print(f'inclui o numero 0 depois do num 3 aumentando os valores da lista {num}')
#remoção de elementos
# num.pop()
# print(f'Remove o ultimo valor da lista {num}')
num.pop(2)
print(f'Remove o segundo item da lista, nesse exemplo o numero 0 some {num}')
num.insert(2,2)
print(f'inclui o numero 2 na segunda posição da lista {num}')
num.remove(2)
print(f'Remove o primeiro numero 2 da lista {num}')#para remover todos os itens iguais faça um laço for.
# num.remove(4) #ValueError: list.remove(x): x not in list
# print(num)
# if 4 in num: # também remove apenas o primeiro iten encontrado da lista
#     num.remove(4)
# else:
#     print('Não achei o numero 4 na lista.')
#
# if 2 in num:  #teste com outro numero
#     num.remove(2)
#     print(f'Numero 2 removido com sucesso!{num}')
# else:
#     print('Não achei o numero 2 na lista.')
# valores = list()#cria uma lista vazia
# valores = []#cria uma lista vazia
# valores.append(5)
# valores.append(9)
# valores.append(4)
# print(f'Exibe os valores inseridos na lista {valores}')
# print('Exibe os valores com os ... na frente: ', end='')
# for v in valores:
#     print(f'{v}...',end='')
# #para mostrar a posição do valor incluso na lista:
# for p, v in enumerate(valores):
#     print(f'\nNa posição {p} encontrei o valor {v}')
# for c in range(0,5): #solicita valores, a quantidade deve ser definida dentro do range.
#     valores.append(int(input('Digite um valor: ')))
# for p, v in enumerate(valores):
#     print(f'\nNa posição {p} encontrei o valor {v}')
a = [2,3,4,7]
b = (a) #uma view da lista a
print(f'Lista a: {a}')
print(f'Lista b: uma view da lista a {b}')
#então se eu mexer na lista b automaticamente ele mexerá nas duas, veja:
# b[2]= 8
print('então se eu mexer na lista b automaticamente ele mexerá nas duas, veja:')
print(f'Lista a: {a}')
print(f'Lista b: {b}')
#para fazer uma cópia da lista a na lista b use b=a[:]:
b = a[:]
print(f'Lista a: {a}')
print(f'para fazer uma cópia da lista a na lista b use b=a[:] -> {b}')
b[2] = 8
print(f'lista a: {a}')
print(f'alterações apenas na lista b, veja: {b}')


