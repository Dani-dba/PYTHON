sexo= str(input('Digite o seu sexo:')).strip()
while sexo not in "MF":
    sexo = str(input('Dados invalidos. por favor informe o seu sexo:')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))
print('Fim')