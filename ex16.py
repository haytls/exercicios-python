# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex:
# Digite um número:6.127 o número 6.127 tem a parte inteira 6.
from math import ceil
n =float(input('Digite um número qualquer: '))
print('O número \033[4m{}\033[m tem como parte inteira \033[4m{}\033[m'.format(n, ceil(n)))

