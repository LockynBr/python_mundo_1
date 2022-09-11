#Aumento do salário
salario = float(input('Digite seu salario bruto: '))
aumento = salario * 15 / 100
valortotal = salario + aumento

print('O aumento do seu salario foi de 15%, sendo assim ele foi de R${} para R${:.2f}. Então seu aumento foi de R${}.'.format(salario, valortotal, aumento))