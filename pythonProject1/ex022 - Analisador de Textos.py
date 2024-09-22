nome= str(input('Digite o nome completo:')).strip()

print(nome.upper())
print(nome.lower())
#print(len(nome.replace(' ', '' )))
print (len(nome)-nome.count(' '))
'''dividir = nome.split()
if len(dividir) > 0:
    tpn: str= len(dividir[0])
print(f'o tamanho do primeiro nome é:{tpn}')
else
print('não foi possivel calcular o tamanho do nome')'''
print(nome.find(' '))