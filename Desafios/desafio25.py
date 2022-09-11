#Saber se tem SILVA em qualquer parte do nome
nome = str(input('Digite seu nome completo: ')).strip()

print('Seu Nome tem Silva? {}'.format('SILVA' in nome.upper()))