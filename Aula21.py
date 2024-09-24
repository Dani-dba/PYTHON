# print('olá mundo')
# help(print())
# print(input.__doc__)
# def contador(i, f, p):
#     #cria a docstring informando qual a função da def, os parametros para facilitar o uso de quem for utilizar a def
#     """
#     Esta é uma função de contador e os parametros são
#     :param i: numero inicial da contagem
#     :param f: numero final da contagem
#     :param p: de quantos em quantos numeros a contagem vai pular
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('Fim!')
#
# contador (2, 20, 2)
#
# help(contador) #mostra a docstring criada com a explicação da função.
# def soma(a, b, c):
#     s = a + b + c
#     print(f'{s}')
#
# soma(1, 2, 3)

#Parametros opcionais
# def soma(a=0, b=0, c=0):
#     """
#
#     :param a: Primeiro número da soma
#     :param b: Segundo número da soma
#     :param c: Terceiro número da soma
#     :return: no return
#     """
#     s = a + b + c
#     print(f'A soma vale: {s}')
#
# soma(2,3,)

# Parametros opcionais
# def somar(a=0, b=0, c=0):
#
#     """
#
#     :param a: Primeiro número da soma
#     :param b: Segundo número da soma
#     :param c: Terceiro número da soma
#     :return: no return
#     """
#
#     s = a + b + c
#     return s
#
#
# r1 = somar(2,3,4)
# r2 = somar(2,3)
# r3 = somar(3)
#
# print(f'Os resultados obtidos foram {r1}, {r2} e {r3}')
#

#programa principal para definição de escopo:
# def teste():
#     x = 8 #escopo local
#     print(f'Na funcão teste, n vale {n}')
#     print(f'Na funcão teste, x vale {x}')
#
# n = 2 #escopo global
# print(f'No programa principal n vale {n}')
# print(f'No print não é possivel trazer x nesta linha pois ele foi definido apenas dentro da função teste')
# teste()

#definição de escopo global e local:
# def teste(b):
#     """
#
#     :param a: variavel a no escopo local de teste
#     :param b: variavel b no escopo local de teste
#     :param c: variavel c no escopo local de teste
#     :return: sem retorno
#     """
#     a=8
#     b+=4
#     c=2
#     print(f'A dentro de teste vale {a}')
#     print(f'B dentro de teste vale {b}')
#     print(f'C dentro de teste vale {c}')
#
#
# a = 5
# teste(a)
# print(f'A fora de teste vale {a}')
# print('Variaveis dentro de teste são classificadas como escopo local e fora de teste são escopo global')

# #maneira de globalizar uma variavel local
# def teste(b):
#     """
#
#     :param a: variavel a no escopo local de teste
#     :param b: variavel b no escopo local de teste
#     :param c: variavel c no escopo local de teste
#     :return: sem retorno
#     """
#     global a
#     a=8
#     b+=4
#     c=2
#     print(f'A dentro de teste vale {a}')
#     print(f'B dentro de teste vale {b}')
#     print(f'C dentro de teste vale {c}')
#
#
# a = 5
# teste(a)
# print(f'A fora de teste vale {a}')
# print('neste caso a variavel que foi usada para o valor de A é a variavel de dentro pois foi usado o parametro global')
#
# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
#
# n = int(input('Digite um numero: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}!')
# print(f'Os resultados são {f1}, {f2}, {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
print(par(num))


