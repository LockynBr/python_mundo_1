#Adicionar uma ordem aleatoria
from random import shuffle

aluno1 = str(input('Digite o número do Aluno 1:'))
aluno2 = str(input('Digite o número do Aluno 2:'))
aluno3 = str(input('Digite o número do Aluno 3:'))
aluno4 = str(input('Digite o número do Aluno 4:'))
names = [aluno1, aluno2, aluno3, aluno4]
shuffle(names)

print('Dos alunos {}, {}, {}, {} a ordem de apresentação será de {}'.format(aluno1, aluno2, aluno3, aluno4, names))