#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder,
#mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
from random import randint
v = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
while True:
    j = int(input('Diga um valor: '))
    c = randint(0, 10)
    s = j + c
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I] ? ')).strip().upper()[0]
    print('-' * 30)
    print(f'Você jogou {j} e o computador {c}. Total de {s}')
    print('-' * 30)
    if tipo == 'P':
        if s % 2 == 0:
            print('\033[33mVocê venceu!\033[m')
            print('Jogue novamente...')
            print('=-'*15)
            v += 1
        else:
            print('\033[31mVocê perdeu\033[m')
            break
    elif tipo == 'I':
        if s % 2 != 0:
            print('\033[33mVocê venceu!\033[m')
            print('Jogue novamente...')
            print('=-' * 15)
            v += 1
        else:
            print('\033[31mVocê perdeu\033[m')
            break
print(f'\033[31mGame Over!\033[m Você venceu {v} vezes.')

