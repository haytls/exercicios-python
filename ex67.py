#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
m = 0
while True:
    print('-'*40)
    n = int(input('Quer ver a tabuada de qual valor ? '))
    print('-'*40)
    if n < 0:
        print('Programa tabuada encerrado. Volte sempre!')
        break
    for c in range(1, 11):
        m = n * c
        print(f'{n} X {c} = {m}')