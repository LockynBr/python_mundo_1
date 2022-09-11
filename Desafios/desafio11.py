#Pintura Parede
larg = float(input('Qual a Largura da sua Parede em metros? '))
altu = float(input('Qual a Altura da sua Parede em metros? '))
area = (larg * altu)
ltt = (area / 2)

print('Sua área é {}m²'.format(area))
print('É necessario {}L de tinta para pintar {}m²'.format(ltt, area))