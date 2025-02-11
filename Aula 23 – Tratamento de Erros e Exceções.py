try:
    a = int(input('Numerador:'))
    b = int(input('Denominador:'))
    r = a/b
except Exception as erro:
    print('Infelizmente tivemos um problema :(')
    print(f'O problema encontrado foi {erro.__class__}')
# except
#     print(f'O problema encontrado foi {erro.__class__}')
else:
    print(f'o resultado é {r:.1f}')
finally:
    print('Volte sempre, muito obrigado :)')