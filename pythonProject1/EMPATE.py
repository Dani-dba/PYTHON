'''print('\033[33mEMPATE!\033[m')'''
'''while True:
    print("=" * 30)
    print("MENU")
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair do programa")
    print("=" * 30)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 5:
        print("Saindo do programa...")
        break

    if opcao < 1 or opcao > 5:
        print("Opção inválida! Por favor, escolha uma opção válida.")
        continue

    if opcao == 4:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        continue

    if opcao == 1:
        print("A soma dos valores é:", valor1 + valor2)
    elif opcao == 2:
        print("A multiplicação dos valores é:", valor1 * valor2)
    elif opcao == 3:
        print("O maior valor é:", max(valor1, valor2))'''
from random import randint
n = randint(10,100)
print(n)
