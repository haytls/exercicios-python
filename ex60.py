#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#ex:
#5! = 5x4x3x2x1 = 120
n = int(input('Digite um número: '))
f = 1
# print('o Faratorial de {} é {}'.format(n, s))
while n > 0:
    f *= n
    n -= 1
print('O fatorial desse número é {}'.format(f))
