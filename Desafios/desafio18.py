#Calculo seno, cosseno, tangente
from math import radians, sin, cos, tan
ang = float(input('Digite um angulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print('Seu angulo é {}. Seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}.'.format(ang, seno, cosseno, tangente))