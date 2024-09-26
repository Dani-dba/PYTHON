def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações dos alunos:
    *n: Notas
    sit: Situação do aluno
    Returns: retorno das notas e a situação do aluno com média

    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r

resp = notas(5.5, 2.2, sit=True)
print(resp)

help(notas)