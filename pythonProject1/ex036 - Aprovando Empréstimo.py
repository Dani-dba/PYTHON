valor_emprestimo = float(input('Digite o valor solicitado:'))
salario_cliente = float(input('Qual o seu salario atual?:'))
tempo_pagamento = int(input('Em quantos anos deseja concluir o pagamento:'))
prestacao_mensal = valor_emprestimo/(tempo_pagamento*12)
percentual_emprestimo = prestacao_mensal*100/salario_cliente
if percentual_emprestimo >= 30:
    print('Empréstimo NEGADO!')
else: print('Parabéns, seu empréstimo foi aprovado!')
