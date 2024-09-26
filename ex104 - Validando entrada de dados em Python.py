def leiaint(msg):
    ok = False
    valor =0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;031mERRO! Digite um numero inteiro válido!\033[m')
        if ok:
            break
    return valor

#programa principal
n = leiaint('Digite um Número: ')
print(f'Você acabou de digitar o número {n}')