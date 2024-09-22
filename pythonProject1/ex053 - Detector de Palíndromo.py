frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Você digitou a frase {}'.format(junto))
inverso = ''
for letra in range (len(junto)-1, -1, -1):
   inverso = inverso + junto[letra]
if junto == inverso:
       print ('A frase digitada é um PALINDROMO!')
else:
       print ('A frase digitada não é um PALINDROMO!')
print(inverso, junto)