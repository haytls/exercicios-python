#Escreva um programa que faça  o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
#escolhido pelo computador.

#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
n =int(input('Adivinhe o número: '))
nm = random.randint(0, 5)
print('Número escolhido pela maquina: {}'.format(nm))
if n == nm:
    print('\033[32mVocê venceu\033[m')
else:
    print('\033[31mVocê perdeu\033[m')

