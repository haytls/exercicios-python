#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras em maúsculas. O nomde com todas minúsculas.
# Quantas letras ao tod.
#  (sem considerar espaços). Quantas letras tem o primeiro nome.
nome =str(input('DIgite seu nome: ')).strip()
print('\033[7mSeu nome em maiúsculo é {}\033[m'.format(nome.upper()))
print('\033[31;45mSeu nome em minúsculo é {}\033[m'.format(nome.lower()))
print('\033[33;40mSeu nome tem ao todo {} letras\033[m'.format(len(nome) - nome.count(' ')))
print('\033[4mO seu primeiro nome tem {} letras\033[m'.format(nome.find(' ')))



