from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range (1,8):
    nasc = int(input('Digite o ano de nascimento da {}º pessoa:'.format(c)))
    idade = atual - nasc
    if idade >=18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1

print('Tivemos um total de {} pessoas maiores.'.format(totmaior))
print('Tivemos um total de {} pessoas menores.'.format(totmenor))
