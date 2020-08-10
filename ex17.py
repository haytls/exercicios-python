# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
cp =float(input('Digite o comprimento do cateto oposto: '))
ca =float(input('Digite o comprimento do cateto adjacente: '))
h =math.hypot(cp, ca)
print('O cateto oposto é {}, já o adjacente é {}, por fim a hipotenusa é {:.2f}'.format(cp, ca, h))



