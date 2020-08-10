# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex:
# Digite um número:6.127 o número 6.127 tem a parte inteira 6.
from math import floor
n =float(input('Digite um número qualquer: '))
print('O número {} tem como parte inteira {}'.format(n, floor(n)))

