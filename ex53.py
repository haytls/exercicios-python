#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j) -1, -1, -1):
    i = i + j[l]
print('O inverso de {} é {}'.format(j, i))
if i == j:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!' )