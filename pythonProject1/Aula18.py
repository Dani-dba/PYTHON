# teste = list() #cria lista teste
# teste.append('Gustavo') #inclui gustavo em teste no dicionario 1
# teste.append(40) #inclui a idade 40 no dicionario 2
# print(teste) #exibe ['Gustavo', 40]
# galera = list() #cria a lista galera vazia
# galera.append(teste) #faz uma view da lista teste dentro da lista galera
# print(galera) # exibe [['Gustavo', 40]]
# teste [0] = 'Maria' #altera o dicionario 1 de teste de gustavo para maria
# teste[1] = '22' #altera o dicionario 2 de teste de 40 para 22
# galera.append(teste) #inclui mais uma view de teste em galera
# print(galera) #exibe [['Maria', '22'], ['Maria', '22']] pois teste foi alterado em sua raiz e galera é apenas uma visualização da lista teste
#esquece tudo e começa de novo
# teste=list() #cria uma lista vazia pra teste
# teste.append('Gustavo') #inclui gustavo em teste no dicionario 1
# teste.append('40') #inclui 40 em teste no dicionario 2
# galera=list() #cria a lista galera vazia
# galera.append(teste[:]) #copia os dados de teste em galera
# teste[0]='Maria' #altera o dicionario 0 de teste de gustavo para maria
# teste[1]='22' #altera o dicionario 1 de teste de 40 para 22
# galera.append(teste[:]) #copia os dados alterados de teste para galera mantendo a cópia anterior e criando outro campo na lista
# print(galera)#exibe os dois campos da lista
# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] #cria uma estrutura com varios dados dentro "uma estruturona com varias estruturazinhas'
# print(galera) #exibe [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera[0][0]) #exibe João
# print(galera[2][1]) #exibe 13, idade do joaquim
# print(galera [3][0]) #exibe Maria
# print(galera[1][0])
# for p in galera: #imprime somente os nomes
#     print (p[0])
# for p in galera: #imprime a lista completa
#     print(p)
# for p in galera: #imprime a lista formatada.
#     print(f'{p[0]} tem {p[1]} anos de idade')
# galera = list()
# dado = list()
# for c in range (0,3):
#     dado.append(str(input('Nome:')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:]) #se eu não botar os : ele vai gerar lista vazia conforme prox exemplo.
#     dado.clear()
# print(galera)
# galera = list()
# dado = list()
# for c in range (0,3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado) #cria lista vazia pq não foi feita uma copia de dado, apenas uma visualização dela
#     dado.clear() #aqui o dado é apagado gerando a lista vazia.
# print(galera)
totmai = totmen = 0 #posso fazer com variavel simples mas não posso fazer com variaveis compostas, ou listas
galera = list()
dado = list()
for c in range (0,3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #se eu não botar os : ele vai gerar lista vazia conforme exemplo acima.
    dado.clear()
# print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade ')
print(galera)
