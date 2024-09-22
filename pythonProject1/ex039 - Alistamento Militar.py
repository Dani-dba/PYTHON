from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE')
elif idade < 18:
    saldoa = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldoa))
elif idade > 18:
    saldob = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldob))
