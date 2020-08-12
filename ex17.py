# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
cp =float(input('Digite o comprimento do cateto oposto: '))
ca =float(input('Digite o comprimento do cateto adjacente: '))
h =math.hypot(cp, ca)
print('O cateto oposto é \033[45m{}\033[m, já o adjacente é'
      ' \033[45m{}\033[m, por fim a hipotenusa é \033[45m{:.2f}\033[m'.format(cp, ca, h))



