salario_original = float(input('Insira o salario original:'))
percentual_aumento = int(input('Qual o percentual de aumento?'))
fator_aumento = percentual_aumento / 100
valor_com_aumento = salario_original * (1 + fator_aumento)
print('O salario com aumento é {:.2f}'.format(valor_com_aumento))

'''salário = float(input('Qual é o salário do funcionário? RS'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava RS{:.2f}, com aumento passa a receber RS{:.2f}'.format(salário, novo))'''
