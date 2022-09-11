#Preço da viagem com desconto de determinada kilometragem
viagem = float(input('Qual a distancia da sua viagem em KM: '))

if viagem <= 200:
    preco = 0.50 * viagem
    print('Sua viagem tem {}KM e o total dela é de R${:.2f}.'.format(viagem, preco))
else:
    preco = 0.45 * viagem
    print('Sua viagem tem {}KM e o total dela é de R${:.2f}.'.format(viagem, preco))