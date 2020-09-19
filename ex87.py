#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os números pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = maior = somac = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista [l] [c]:^6}]', end='')
        if lista[l][c] % 2 == 0:
            soma += lista[l][c]
    print()
for l in range(0, 3):
    somac += lista[l][2]
for c in range(0, 3):
    if c == 0:
        maior = lista[1][c]
    else:
        if lista[1][c] > maior:
            maior = lista[1][c]
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {somac}')
print(f'O maior valor da segunda linha é {maior}')
