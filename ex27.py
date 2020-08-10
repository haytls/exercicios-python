#Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro nome e o último nome separadamente.
#Ex: Ana Maria Souza
#Primeiro = Ana
#Segundo = Souza
nome =str(input('Digite seu nome: '))
s = nome.split()
print('Seu primeiro nome = {}'.format(s[0]))
print('Seu segundo nome = {}'.format(s[len(s)-1]))






