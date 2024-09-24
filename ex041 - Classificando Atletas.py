from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento:'))
idade = (atual - ano)
print('O atleta tem {} anos.'.format(idade))
print('Categoria:')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <=19:
    print('Junior')
elif idade <=20:
    print('Senior')
else:
    print('Master')
