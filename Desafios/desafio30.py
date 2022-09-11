#Mostrar se o número digitado é impar ou par
num = int(input('Digite um número inteiro: '))

if (num%2) == 0:
    print('O numéro {} é Par.'.format(num))
else:
    print('O número {} é Impar.'.format(num))