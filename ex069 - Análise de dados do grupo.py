idade = 0
sexo = ''
continua = ''
cont_18 = 0
cont_m = 0
cont_f_20 = 0
while True:
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite o sexo: [F/M]:')).upper().strip()
    continua = str(input('Deseja continuar? [S/N]:')).upper().strip()
    if idade > 18:
        cont_18 += 1
    if sexo == 'M':
        cont_m += 1
    if sexo == 'F' and idade < 20:
        cont_f_20 += 1
    if continua == 'N':
        break
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]:')).upper().strip()
print(f'Foram cadastradas {cont_18} pessoas maiores de 18 anos, {cont_m} homens e {cont_f_20} mulheres com menos de 20 anos.')
