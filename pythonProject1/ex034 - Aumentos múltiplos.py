salario = float(input('Digite o salario do funcionario: '))
if salario <= 1250:
    aumento = salario + (salario * 15/100)
else:
    aumento = salario + (salario* 10/100)
print('o novo salário será de {} R$'.format(aumento))