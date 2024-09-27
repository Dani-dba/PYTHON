import uteis

#Programa principal
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
dob = uteis.dobro(num)
tri = uteis.triplo(num)

print(f'O fatorial de {num} é igual a {fat}')
print(f'O dobro de {num} é igual a {dob}')
print(f'O triplo de {num} é igual a {tri}')