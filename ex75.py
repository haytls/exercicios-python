#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
print('Digite 4 valores!')
n = (int(input('Primeiro valor: '))), (int(input('Segundo valor: '))), (int(input('Terceiro valor: '))), (int(input('Quarto valor: ')))
print(f'você digitou os valores{n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print('OS valores pares digitados foram: ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
