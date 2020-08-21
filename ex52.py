#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        t = t + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divísivel {} vezes'.format(n, t))
if t == 2:
    print('Por isso ele É primo!')
else:
    print('Por isso ele NÃo é primo!')
