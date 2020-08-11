# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
n =int(input('Digite um número:'))
print('O sucessor é \033[0;31m{}\033[m e o antecessor é \033[0;31m{}\033[m'.format((n+1), (n-1)))

