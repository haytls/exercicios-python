#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamnete.
#Ao final, mostre o contúdo das três listas geradas.
lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
for v in lista:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'A lista apenas com números pares é {par}')
print(f'A lista apenas com números impares é {impar}')