#Transformar 
nome = input('Digite seu nome completo: ')
nomesemesp = nome.replace(" ", "")
dividido = nome.split()

print('Seu nome em maiusculo é: ', nome.upper())
print('Seu nome em minusculo é: ', nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nomesemesp)))
print('Seu primeiro nome é {} e tem {} letras'.format(dividido [0], len(dividido [0])))