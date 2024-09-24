from datetime import date
cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
cadastro['ano_nasc']= int(input('Ano de nascimento: '))
cadastro['Idade'] =  (date.today().year) - cadastro['ano_nasc'] #pode ser usado o datetime com o now = datetima.now().year
cadastro['Carteira'] = int(input('Carteira de trabalho (0 = não tem): '))
if cadastro['Carteira'] != 0:
    cadastro['ano_contratacao'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['ano_contratacao'] + 35) - date.today().year)

print('-=' * 30 )
for k, v in cadastro.items():
    print(f' -{k} tem o valor {v}')