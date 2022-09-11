#Valor da multa quando passar de 80KM/h
velocidade = float(input('Qual a velocidade do veículo em KM/h: '))
via = 80
if velocidade <= 80:
    print('O veículo está a {}KM/h que é a velocidade da via.'.format(velocidade))
else:
    subvel = velocidade - 80
    multa = subvel * 7
    print('O veículo ultrapassou a velocidade da via que é de {}KM/h, sendo assim você tomou multa no valor dela é R${:.2f}.'.format(via, multa))
