#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
cont = 0
while True:
    lista.append(int(input('Digite um número: ')))
    cont += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar ? ')).strip().upper()[0]
    if c == 'N':
        break
print(f'Foram digitados {cont} valores!')
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente ficam assim:\n{lista}')
if  5 in lista:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado!')