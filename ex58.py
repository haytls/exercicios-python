#Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
v = 0
s = 0
a = randint(1, 10)
print('Vamos brincar!!')
while v != a:
    v = int(input('Tente adivinhar o número escolhido pela maquina: '))
    s += 1
print('\033[32mParabéns você acertou\033[m, mas a quantidade de vezes que você tentou até acertar foi {}'.format(s))