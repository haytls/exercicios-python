#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 =int(input('Digite um número: '))
num2 =int(input('Digite outro: '))
num3 =int(input('Digite mais um: '))
# Verificando quem é o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# Verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('\033[33mO menor número é {}\033[m'.format(menor))
print('\033[33mO maior número é {}\033[m'.format(maior))


