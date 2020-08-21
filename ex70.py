#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre.
#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$1000.
#C) Qual é o nome do produto mais barato.
total = mais = precomais = quant = 0
barato = " "
print('-'*30)
print('LOJA MEU PAL NA TUA MÃO')
print('-'*30)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto R$: '))
    quant += 1
    total += preco
    if preco > 1000:
        mais += 1
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        print('Compra concluida, volte novamente!')
        break
    if quant == 1 or preco < precomais:
        precomais = preco
        barato = nome
print(f'O total gasto foi de {total:.2f}')
print(f'Foram {mais} prodrutos que custaram mais de R$ 1000')
print(f'O produto mais barato foi {barato} de R$ {precomais}')
