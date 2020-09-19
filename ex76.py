#Crie um programa que tenha uma tupla única com nomes de produtos e seus preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*39)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*39)
for posicao in range(len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')
    else:
        print(f'R${listagem[posicao]:.>7.2f}')