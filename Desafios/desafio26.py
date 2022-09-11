#Contar quantas vezes a letra aparece
frase = str((input('Digite uma frase: ')).upper().strip())

print(frase)
print('A letra "A" aparece {} vezes em sua frase.'.format(frase.count('A')))
print('A letra "A" aparece sua primeira vez na posição {}.'.format(frase.index('A')+1)) 
print('A letra "A" aparece sua última vez na posição {}.'.format(frase.rfind('A')+1))