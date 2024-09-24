lista = []
maior = menor = 0
for v in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {v}:')))
    if v == 0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        if lista[v] < menor:
            menor = lista[v]
print(f'Você digitou os valores {lista}')
print(f' o maior valor é {maior} nas posições: ', end='')
for p, v in enumerate(lista):
    if v == maior:
        print(f' {p} e ', end='')
print(f' o menor valor é {menor} nas posições: ', end='')
for p, v in enumerate(lista):
    if v == menor:
        print(f' {p} e ', end='')




