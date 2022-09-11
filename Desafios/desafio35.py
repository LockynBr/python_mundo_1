#Saber se é possivel formar um triângulo com 3 lados
l1 = float(input('Digite um lado: '))
l2 = float(input('Digite outro lado: '))
l3 = float(input('Digite outro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É possivel formar um triângulo')
else:
    print('Não é possivel formar um triângulo')