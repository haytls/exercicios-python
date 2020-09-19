# Faça um programa que tenha um a lista chamada números e duas funções chamadas sorteia() e soma par(). A primeira função vai sortear 5 núemros
# e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint

lista = []


def sorteia():
    s = soma = 0
    print('\nSorteando 5 valores:', end='')
    for c in range(1, 6):
        s = randint(0, 10)
        lista.append(s)
        print(f' {s}', end='')
    print(' Pronto!')
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia()
