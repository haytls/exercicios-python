#Refaça o desafio 9, mostrando a tabuada de um número que o usuario escolher, só que agora utilizando um laço for.
n = int(input('Digite um número: '))
for c in range(0, 11):
    m = n * c
    print('{} X {} = {}'.format(n, c, m))
