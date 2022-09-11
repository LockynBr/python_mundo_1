#Jogo de erro ou acerto com a máquina
from time import sleep
from random import randint

num = int(input('Digite um número de 0 a 5: '))
rnd = randint(0, 5)

print('-=-' * 8)
print('PENSANDO EM UM NÚMERO...')
print('-=-' * 8)

print('PROCESSANDO...')
sleep(3) # faz o programa demorar para mandar o próximo print.

if num == rnd:
    print('Acertou na mosca! O número foi pensado foi o {}.'.format(rnd))
else:
    print('Errou feio. O número pensando foi o {} e não {}.'.format(rnd, num))
print('FIM')