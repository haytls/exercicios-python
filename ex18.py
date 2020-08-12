# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input('Digite um ângulo: '))
c = math.cos(a)
s = math.sin(a)
t = math.tan(a)
print('O ângulo \033[4;31m{}°\033[m tem como cosseno \033;31m{:.2f}\033[m,'
      'como seno \033[4;31m{:.2f}\033[m e como tangente \033[4;31m{:.2f}\033[m'.format(a, c, s, t))

