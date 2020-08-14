#Crie um programa que faça o computador jogar jokenpô com você.
from random import randint
from time import sleep
print("""Suas opções 
[ 0 ] Pedra 
[ 1 ] Papel 
[ 2 ] Tesoura""")
play = int(input('Qual a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
lista = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('+-'*14)
print('O computador escolheu {}'.format(lista[computador]))
print('Você escolheu {}'.format(lista[play]))
print('+-'*14)
if computador == 0:
    if play == 0:
        print('EMPATE!')
    elif play == 1:
        print('VOCÊ VENCEU')
    elif play == 2:
        print('O COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁVILA!')
elif computador == 1:
    if play == 0:
        print('O COMPUTADOR VENCEU')
    elif play == 1:
        print('EMPATE!')
    elif play == 2:
        print('VOCÊ VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if play == 0:
        print('VOCÊ VENCEU')
    elif play == 1:
        print('O COMPUTADOR VENCEU')
    elif play == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA')



