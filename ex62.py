#Melhore o desfafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
m = 10
t = 0
while m != 0:
    t += m
    while c <= t:
        print('{} |'.format(p), end="")
        p += r
        c += 1
    print('Você quer mostrar mais termos ?')
    m = int(input('Se sim quantos ? '))
    p += r
print('ACABOU!!')
