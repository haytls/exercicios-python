#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*num):
    mais = 0
    print('=-'*30)
    print('Analisando os valores passados...')
    tam = len(num)
    for valor in num:
        sleep(0.5)
        print(f'{valor} ', end='')
        sleep(0.4)
        if tam == 1:
            mais = valor
        else:
            if valor > mais:
                mais = valor
    print(f'Foram digitados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mais}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(0)