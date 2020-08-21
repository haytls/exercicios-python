#Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.
p = int(input('Digite o primeiro número: '))
r = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    print('{} |'.format(p), end=" ")
    p += r
    cont += 1
print('FIM')