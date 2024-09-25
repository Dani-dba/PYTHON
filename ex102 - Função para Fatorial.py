def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um numero
    Args:
    n: numero a ser calculado
    show: exibir o calculo
    Returns: O resultado do fatorial

    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print('x', end='')
            else:
                print('=', end='')
        f *= c
    return f
n = int(input('Digite um numero para calcular o fatorial: '))
print(f'{fatorial(n, show=True)}')
help(fatorial)
