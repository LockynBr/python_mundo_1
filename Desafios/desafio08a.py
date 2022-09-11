#Transformações metricas.
valor = float(input('Digite sua medida em metros: '))

print('{}KM \n{}HM \n{}DAM \n{}M \n{}DM \n{}CM \n{}MM'.format(valor / 1000, valor / 100, valor / 10, valor, valor * 10, valor * 100, valor * 1000))