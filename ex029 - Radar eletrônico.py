velocidade = int(input('Digite a velocidade: '))
excedente = velocidade - 80

#print('Boa viagem, dirija com segurança' if velocidade <= 80 else 'MULTADO! Você ultrapassou o limite que é de 80km/h {} R$'.format(custo))
if velocidade > 80:
    print('MULTADO! Você ultrapassou o limite que é de 80km/h')
    print('-'*100)
    multa = excedente * 7
    print('O valor da multa será de {} R$'.format(multa))

print('Boa viagem, dirija com segurança')
