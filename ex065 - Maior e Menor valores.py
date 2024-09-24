soma = 0
contador = 0
continua = 'S'
maior = menor = 0
while continua == 'S':
    n = int(input('Digite um valor: '))
    soma += n
    contador +=1
    if contador == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continua = str(input('Deseja continuar? S/N ')).upper()
    while continua != 'S' and continua != 'N':
        continua = str(input('Opção inválida, deseja continuar? S/N ')).upper()
media = soma / contador
print('{} numeros digitados.'.format(contador))
print('A média dos valores digitados é igual a: {}'.format(media))
print('O maior valor digitado foi: {} '.format(maior))
print('O menor valor digitado foi: {} '.format(menor))


