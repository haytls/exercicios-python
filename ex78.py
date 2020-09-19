#Faça um programa que leia 5  valores númericos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições.
valor = []
maior = menor = 0
for c in range(0, 5):
    valor.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = valor[c]
    else:
        if valor[c] > maior:
            maior = valor[c]
        elif valor[c] < menor:
            menor = valor[c]
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}...', end='')

