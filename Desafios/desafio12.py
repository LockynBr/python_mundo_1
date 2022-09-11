#Desconto Produto
pdt = float(input('Qual é o preço do produto? R$'))
desconto = (pdt * 5 / 100)
valortotal = pdt - desconto

print('O preço do produto após o desconto de 5% é R${:.2f}. Então você economizou R${:.2f}.'.format(valortotal, desconto))
