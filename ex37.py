#Escreva um programa que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão:
#-1 para binário:
#-2 para octal:
#-3 para hexadecimal:
import math
num = int(input('Digite um numero inteiro: '))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para Binário
[ 2 ] converter para octal 
[ 3 ] converter para hexadecimal""")
op = int(input('Opção: '))
if op == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif op ==3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, digite outro número.')



