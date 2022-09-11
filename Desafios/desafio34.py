#Aumento do salário de acordo com o salário atual
salario = float(input('Digite seu salário R$'))
aumento1 = salario + salario * 0.10 # As suas funcionam
aumento2 = salario + (salario * 15 / 100) # Tecnica mais simplificada

if salario >= 1250.00:
    print('Seu salario era R${:.2f} e passou a ser R${:.2f}.'.format(salario, aumento1))
else:
    print('Seu salario era R${:.2f} e passou a ser R${:.2f}.'.format(salario, aumento2))