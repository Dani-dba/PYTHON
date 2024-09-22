#
# def soma (a, b):
#     print(f'A = {a} B = {b}')
#     s = a + b
#     print(f'A soma vale {s}')
# # programa principal
#
#
# a = 4
# b = 5
# s = a + b
# print(s)
# soma (4,5) #mesma coisa, só que na def
#
# a = 8
# b = 9
# s = a + b
# print(s)
# soma (8,9)
#
# a = 2
# b = 1
# s = a + b
# print(s)
# soma(2,1)
# soma(b=10, a=5)
#

# def contador(*num):
#     for valor in num:
#         print(f'{valor} ', end='')
#     print(end=' ')
#     # print('Fim')
#     tam = len(num)
#     print(f'Recebi os valores {num} e são {tam} números ')
#
# contador (2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)
#
# def dobra(lst): #lista
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos +=1
#
#
# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)
#
def soma(*valores): #desempacotamento
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} é igual a {s}')


soma(5,2)
soma(2, 9, 4)

#mostralinha
# def lin ():
#     print('-' * 30)
#
# lin()
# print('CURSOEMVIDEO')
# lin()

# def titulo(txt):
#     print('-'*len(txt))
#     print(txt)
#     print('-'*len(txt))

# titulo('Danielle')
# titulo('Python é muito bom')


