#Mostras letras do nome
n= str((input('Digite Seu Nome Completo: '))).strip()
nome = n.split()
print('Prazer {}!'.format(nome [0]))
print('Seu Primeiro nome é: {}.\nÚltimo nome é : {}.'.format(nome [0], nome[len(nome)-1]))