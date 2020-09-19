#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em um lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
cadastro = []
dados = []
pesado = leve = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print(f'Foram cadastradas {len(cadastro)} pessoas')
print(f'O maior peso foi de {pesado} do ', end=' ')
for p in cadastro:
    if p[1] == pesado:
        print(f'{p[0]}', end='e ')
print(f'\nO menor peso foi de {leve} do ', end=' ')
for p in cadastro:
    if p[1] == leve:
        print(f'{p[0]}', end='e ')