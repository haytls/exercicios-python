# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Deseja continuar[S/N] ? ')).upper()
# print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar+= 1

print('A quantidade de números pares digitados foi de {} e de impares {}.'.format(par, impar))
