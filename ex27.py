#Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro nome e o último nome separadamente.
#Ex: Ana Maria Souza
#Primeiro = Ana
#Segundo = Souza
nome =str(input('Digite seu nome: '))
s = nome.split()
print('Seu primeiro nome = \033[34m{}\033[m'.format(s[0]))
print('Seu segundo nome = \033[34m{}\033[m'.format(s[len(s)-1]))






