n = s = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1
# print('A soma vale {}'.format(s))
print(f'A soma vale {s} de {cont} números ')
nome = 'José'
idade = 33
salario = 987.35
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}.')
print('O {} tem {} anos.'.format(nome, idade))