#Faça um programa que tenha uma função chamada área(), que receba as dimensôes de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def área():
    s = a * b
    print(f'O terreno com a largura de {a}m e com comprimento de {b}m\nTem a área de {s}m²')


print('-'*30)
print('Controle de Terreno')
print('-'*30)
a = int(input('Digite a largura do terreno [m]: '))
b = int(input('Digite o comprimento do terreno [m]: '))
área()