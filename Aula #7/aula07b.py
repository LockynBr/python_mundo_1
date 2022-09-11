from traceback import print_tb


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e portencia {}'.format(di, e))
#print('A soma vale {}'.format(n1+n2))