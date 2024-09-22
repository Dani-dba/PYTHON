from time import sleep
n1 = int(input('Digite o Primeiro valor:'))
n2 = int(input('Digite o Segundo valor:'))
opção = 0
maior = ''
while opção !=5:
    print('-==-' * 30)
    print('=' * 10, 'Suas opções:', '=' * 10)
    opção = int(input('[1] Soma\n'
                      '[2] Multiplicação\n'
                      '[3] Maior\n'
                      '[4] Novos Números\n'
                      '[5] Sair do programa\n'
                      'Digite a opção desejada:'))
    if opção == 1:
        resultado = n1+n2
        print("A soma entre {} e {} é igual a {}".format(n1,n2, resultado))
    elif opção == 2:
        resultado = n1 * n2
        print('O resultado de {}x{} é igual a {}'.format(n1, n2, resultado))
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print('O maior numero entre {} e {} é {}'.format(n1, n2, maior))
        else:
            resultado = n2
            print('O maior numero digitado é {}'.format(n2))
    elif opção == 4:
        n1 = int(input('Digite o novo numero:'))
        n2 = int(input('Digite outro novo numero:'))
    elif opção == 5:
        print('Finalizando o programa...')
        sleep(2)
        print('Fim do programa!')
    else:
        print('Opção invalida, tente novamente!')
