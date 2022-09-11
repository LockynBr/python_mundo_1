#Qual o menor e maior número digitado
from re import A


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

#Verificando o que é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando o que é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O MENOR valor digitado foi {}.'.format(menor))
print('O MAIOR valor digitado foi {}.'.format(maior))













'''if n1 >= n2 >= n3:
    print('Número maior {}\nNúmero menor {}.'.format(n1, n3))
elif n1 >= n3 >= n2:
    print('Número maior {}\nNúmero menor {}.'.format(n1, n2))
elif n2 >= n1 >= n3:
    print('Número maior {}\nNúmero menor {}.'.format(n2, n3))
elif n2 >= n3 >= n1:
    print('Número maior {}\nNúmero menor {}.'.format(n2, n1))
elif n3 >= n1 >= n2:
    print('Número maior {}\nNúmero menor {}.'.format(n3, n2))
elif n3 >= n2 >= n1:
    print('Número maior {}\nNúmero menor {}.'.format(n3, n1))'''
