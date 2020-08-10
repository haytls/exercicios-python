# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input('Digite um ângulo: '))
c = math.cos(a)
s = math.sin(a)
t = math.tan(a)
print('O ângulo {}° tem como cosseno {:.2f}, como seno {:.2f} e como tangente {:.2f}'.format(a, c, s, t))

