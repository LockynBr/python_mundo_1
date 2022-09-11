#Aluguel de carro
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Qual a quantidade de Kilometros rodados? '))
diasalug = 60 * dias
kmrodados = 0.15 * km

print('Você alugou o carro por {:.2f} dias e andou {}KMs. O total que você deve pagar é R${:.2f}.'.format(dias, km, diasalug + kmrodados))