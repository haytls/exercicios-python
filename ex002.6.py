# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
d =float(input('Quantos reais você tem R$ '))
print('Convertendo \033[4;37mR${:.2f}\033[m reais para dolar fica \033[4;37mUS${:.2f}\033[m dolas'.format(d, (d/3.27)))


