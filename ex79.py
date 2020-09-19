#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número exista lá dentro,
#ele não será adcionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = []
s = 0
while True:
    n = (int(input('Digite valores: ')))
    if n not in valores:
        valores.append(n)
        print('Esse valor foi adcionado com sucesso...')
    else:
        print('Esse valor já havia sido digitado. Tente novamente...')
    continuar = " "
    while continuar not in 'SN':
        continuar = str(input('Vocẽ deseja continuar [S/N] ? ')).strip().upper()[0]
    if continuar == 'N':
        break
valores.sort()
print(f'Vocẽ digitou os valores {valores}')