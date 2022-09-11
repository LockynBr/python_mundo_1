#Calculo da hipotenusa
'''cttoposto = float(input('Digite o valor do Cateto Oposto: '))
cttadja = float(input('Digite o valor do Cateto Adjacente: '))
hipt = (cttoposto ** 2 + cttadja ** 2) ** (1/2)

print('A soma dos catetos que forma a hipotenusa é igual a {:.2f}.'.format(hipt))'''

from math import hypot
cttoposto = float(input('Digite o valor do Cateto Oposto: '))
cttadja = float(input('Digite o valor do Cateto Adjacente: '))
hipt = hypot(cttoposto, cttadja)

print('A soma dos catetos que forma a hipotenusa é igual a {:.2f}.'.format(hipt))