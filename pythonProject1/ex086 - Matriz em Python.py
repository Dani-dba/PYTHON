# num = [[], [], []]
# matriz0 = []
# matriz1 = []
# matriz2 = []
# cont0 = cont1 = cont2 = 0
# for m1 in range(0,3):
#     num[0].append(int(input(f'Digite um valor para a posição [0, {cont0}]:')))
#     cont0 += 1
#     matriz0.append(num[0][:])
#     num[0].clear()
# for m2 in range(0,3):
#     num[1].append(int(input(f'Digite um valor para a posição [1, {cont1}]:')))
#     cont1 += 1
#     matriz1.append(num[1][:])
#     num[1].clear()
# for m3 in range(0,3):
#     num[2].append(int(input(f'Digite um valor para a posição [2, {cont2}]:')))
#     cont2 += 1
#     matriz2.append(num[2][:])
#     num[2].clear()
# print(matriz0)
# print(matriz1)
# print(matriz2)

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um numero para a posição {[l]}{[c]}: '))
print('-='*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()