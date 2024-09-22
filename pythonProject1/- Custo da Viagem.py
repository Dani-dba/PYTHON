distancia = float(input('Digite a distancia da viagem: '))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O custo total da sua viagem será de {}'.format(preço))
print('Boa Viagem!')