# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p =float(input('Valor do produto R$'))
print('Acrescentando a promoção o valor do produte é R$ \033[4;30;41m{:.2f} reaiss\033[m '.format(p-(p*0.05)))


