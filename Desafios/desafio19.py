#Escolher alguém aleatoriamente.
from random import choice

al1 = str(input('Nome do aluno 1: '))
al2 = str(input('Nome do aluno 2: '))
al3 = str(input('Nome do aluno 3: '))
al4 = str(input('Nome do aluno 4: '))
names = [al1, al2, al3, al4]
escolhido = choice(names)
print('De {}, {}, {} e {} o sorteado para pagar o quadro foi {}.'.format(al1, al2, al3, al4, escolhido))