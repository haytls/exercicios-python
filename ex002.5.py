# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n =int(input('Digite um número: '))
cores= {'limpa':'\033[m', 'cor':'\033[36m'}
print('{} X {:2} e {} '.format(n, cores['cor'], 1, cores['limpa'], (n*1)))
print('{} X {:2} e {} '.format(n, cores['cor'], 2, cores['limpa'], (n*2)))
print('{} X {:2} e {} '.format(n, cores['cor'], 3, cores['limpa'], (n*3)))
print('{} X {:2} e {} '.format(n, cores['cor'], 4, cores['limpa'], (n*4)))
print('{} X {:2} e {} '.format(n, cores['cor'], 5, cores['limpa'], (n*5)))
print('{} X {:2} e {} '.format(n, cores['cor'], 6, cores['limpa'], (n*6)))
print('{} X {:2} e {} '.format(n, cores['cor'], 7, cores['limpa'], (n*7)))
print('{} X {:2} e {} '.format(n, cores['cor'], 8, cores['limpa'], (n*8)))
print('{} X {:2} e {} '.format(n, cores['cor'], 9, cores['limpa'], (n*9)))
print('{} X {:2} e {} '.format(n, cores['cor'], 10, cores['limpa'], (n*10)))
print('{} X {:2} e {} '.format(n, cores['cor'], 0, cores['limpa'], (n*0)))
