def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero intero válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mO usuário não digitou números inteiros..\033[m')
            return 0
        else:
            return n



# num = leiaint('Digite o valor:')
# print(f'O valor digitado foi {num}')


def leiafloat(msg):
  while True:
      try:
          n = float(input(msg))
      except(ValueError, TypeError):
          print('\033[31mErro: Por favor, digite um número real válido.\033[m')
          continue
      except(KeyboardInterrupt):
          print('\n\033[31mUsuário interrompeu o programa\033[m ')
          return 0
      else:
          return n


n1 = leiaint('Digite um numero inteiro: ')
n2 = leiafloat('Digite um numero real:')
print(f'O valor inteiro digitado foi {n1} e o valor real digitado foi {n2}')
