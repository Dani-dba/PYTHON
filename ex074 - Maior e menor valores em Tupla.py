from random import randint
# a = randint(1,10)
# b = randint(1,10)
# c = randint(1, 10)
# d = randint(1,10)
# e = randint(1, 10)
# print(f'{a}, {b}, {c}, {d}, {e}')
# if a>b and a> c and a> d and a>e:
#     print(f'O maior valor da tupla é {a}')
# elif b> a and b>c and b> d and b>e:
#     print(f'O maior valor da tupla é {b}')
# elif c>a and c>b and c>d and c>e:
#     print(f'O maior valor da tupla é {c}')
# elif d>a and d>b and d>c and d>e:
#     print(f'O maior valor da tupla é {d}')
# elif e>a and e>b and e>c and e>d:
#     print(f'O maior valor a tupla é {e}')
# if a<b and a< c and a< d and a<e:
#     print(f'O menor valor da tupla é {a}')
# elif b< a and b<c and b< d and b<e:
#     print(f'O menor valor da tupla é {b}')
# elif c<a and c<b and c<d and c<e:
#     print(f'O menor valor da tupla é {c}')
# elif d<a and d<b and d<c and d<e:
#     print(f'O menor valor da tupla é {d}')
# elif e<a and e<b and e<c and e<d:
#     print(f'O menor valor a tupla é {e}')
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'eu sorteei os valores {n}')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')