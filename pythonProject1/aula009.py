#fatiamento
'''mostra a letra posicionada no espaço do colchete'''
frase = 'curso em video python'
print(frase[0:5])

'''mostra a partir do numero 9 até o numero 12'''
frase = 'Curso em video python'
print(frase[9:13])

'''mostra do numero 9 até a ultima string'''
frase = 'Curso em video Python'
print(frase[9:21])

'''mostra do range nº 9 até o ultimo pulando 2 ranges'''
frase = 'Curso em video python'
print (frase[9:21:2])

'''mostra do primeiro range até o quinto range'''
frase = 'Curso em video python'
print (frase[:5])

'''mostra do 15º range até o ultimo'''
frase = 'Curso em video python'
print(frase[15:])

'''mostra do 9º range até o ultimo, pulando 3 caracteres'''
frase = 'curso em video python'
print(frase[9::3])

#Análise
'''len para mostrar o tamanho da frase, a quantidade de caracteres da string'''
frase = 'Curso em video Python'
print(len(frase))

'''count mostra a quantidade de vezes que a letra digitada em aspas aparece na string'''
frase = 'Curso em video python'
print (frase.count('o'))

'''mostra a quantidade de vezes que a letra digitada em aspas aparece na string desde a range 0 até a 13'''
frase = 'Curso em video python'
print (frase.count('o',0,13))

'''find para localizar um valor especifico dentro da string, 
o resultado é o numero da range inicial do objeto localizado
se o valor procurado não existe o resultado será -1'''
frase = 'Curso em video python'
print(frase.find('deo'))
print(frase.find('android'))

'''operador in diz se o valor existe ou não na string 
resultado em false or true considerando maiusculas e minúsculas'''
frase = 'Curso em video python'
print('Curso' in frase)

#Transformação de string
'''não é possivel alterar o valor original da string, apenas a sua exibição'''
frase= ('Curso em video python')
print(frase.replace('python','android'))

'''upper transforma as letras minusculas da string em letras maiúsculas'''
frase ='Curso em video python'
print(frase.upper())

'''lower transforma letras maiusculas em minusculas'''
frase = 'CURSO EM VIDEO PYTHON'
print(frase.lower())

'''capitalize transforma tudo em minusculo e deixa a primeira em maiusculo '''
frase = 'Curso em vIdEo PythOn'
print (frase.capitalize())

'''title transforma a primeira letra de cada palavra em maiúscula'''
frase = 'curso em videO pytHon'
print(frase.title())

'''strip remove espaços inuteis da string'''
frase = '   Aprenda Python  '
print (frase.strip())
print(frase)

'''rstrip remove espaços inuteis à direita da string'''
frase = 'aprenda python   '
print (frase.rstrip())

'''lstrip remove espaços inuteis à esquerda da string'''
frase = '   aprenda python'
#frase2= '   aprenda python'
print (frase.lstrip())


#Divisões
'''split divide a string, quebra a linha'''
frase = 'Curso em video python'
print(frase.split())

'''join faz a junção do que foi separado no split ou originalmente criado separado'''
frase = 'curso', 'em', 'video', 'python'
print(' '.join(frase))
