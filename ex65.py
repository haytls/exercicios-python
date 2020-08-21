#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
#e qual foi o maior e o menor valor lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n = 0
stop = ''
op = 0
q = 0
m = 0
ma = 0
me = 0
while stop != "N":
    n = int(input('Digite um número: '))
    q += 1
    op += n
    m = op / q
    print('Você deseja continuar ? [S]/[N]')
    stop = str(input('Qual a sua opção: ')).strip().upper()
    if q == 1:
        ma = n
        me = n
    else:
        if n > ma:
            ma = n
        elif n < me:
            me = n
print('A média dos valores apresentados foi de {:.2f}'.format(m))
print('O maior valor apresentado foi de {} e o menor foi o {}'.format(ma, me))