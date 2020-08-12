#Crie um programa que leia o nome de uma pessoa e diga se ele tem "Silva" no nome.
nome =str(input('Digite seu nome: ')).strip()
print('\033[35mSeu nome tem Silva ?\033[m {}'.format('silva' in nome.lower()))
