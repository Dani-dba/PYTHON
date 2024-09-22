'''nome = str(input('Nome: '))'''
somaidade = 0
mediaidade = 0
maioridadehome = 0
nomevelho =''
totmulher20 = 0
for c in range (1,5):
    print('-' * 5 + '{}º pessoa'.format(c) + '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade = somaidade + idade
    if sexo in ['M', 'm']:
        if c == 1:
            maioridadehome = idade
            nomevelho = nome
    if sexo in ['M', 'm'] and idade > maioridadehome:
        maioridadehome = idade
        nomevelho = nome
    if sexo in ['F', 'f'] and idade < 20:
        totmulher20 = totmulher20 + 1


mediaidade = somaidade / 4
print('A média de Idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho, maioridadehome))
print('Temos o total de {} mulheres com menos de 20 anos.'.format(totmulher20))