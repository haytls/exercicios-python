#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.
numero =int(input("Digite um número: "))
resultado = numero % 2
if resultado == 0:
    print('O número digitado é par')
else:
    print('O número digitado é impar')
