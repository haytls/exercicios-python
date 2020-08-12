#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.
numero =int(input("Digite um número: "))
resultado = numero % 2
if resultado == 0:
    print('\033[36mO número digitado é par\033[m')
else:
    print('\033[35mO número digitado é impar\033[m')
