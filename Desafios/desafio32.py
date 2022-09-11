#Saber se o ano é bissexto ou não
from datetime import date
ano = int((input('Em que ano estamos? Coloque 0 para analisar o ano atual: ')))

if ano == 0:
    ano = date.today().year # Peaga o ano atual configurado na máquina.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é Bissexto'.format(ano))
else:
    print('{} não é Bissexto'.format(ano))