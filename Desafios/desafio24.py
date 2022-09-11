#Dizer se existe a palavra SANTO na cidade digitada
city = str(input('Digite o nome da sua cidade: ')).strip()

print(city[:5].upper() == 'SANTO')
