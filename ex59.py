#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] Somar: [2] Multiplicar: [3] Maior: [4] Novos números {5] Sair do programa:
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
op = 0
s = 0
m = 0
ma = 0
n1 = 0
n2 = 0
v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro: '))
while op != 5:
    print("""Escolha o que fazer com esses valores:
    [ 1 ] Somar 
    [ 2 ] Multiplicar 
    [ 3 ] Maior 
    [ 4 ] Novos números
    [ 5 ] Sair do programa""")
    op = int(input('Qual a sua opção ?'))
    if op == 1:
        s = v1 + v1
        print('A soma dos números é de {}'.format(s))
    elif op == 2:
        m = v1 * v2
        print('A multiplicação dos números é de {}'.format(m))
    elif op == 3:
        if v1 > v2:
            ma = v1
        else:
            ma = v2
        print('O maior número é o {}'.format(ma))
    elif op == 4:
        print('Informe os novos valores')
        v1 = int(input('Digite um novo valor: '))
        v2 = int(input('Digite outro: '))

    elif op == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Você digitou um valor de uma opção inexistênte!')
print('Fim do programa, obrigado por utiliza-lo')
