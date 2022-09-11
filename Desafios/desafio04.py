#Tipos
algo = input('Digite algo: ')

print('Seu tipo primitivo é', type(algo))
print('Só tem espaços?', algo.isspace())
print('é um número?', algo.isnumeric())
print('é alfabético?', algo.isalpha())
print('é alfanumérico?', algo.isalnum())
print('Está em maiúscula?', algo.isupper())
print('Está em minúscula?', algo.islower())
print('Está capitalizada?', algo.istitle())
