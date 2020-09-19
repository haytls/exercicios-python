# test = []
# test.append('Gustavo')
# test.append(40)
# galera = []
# galera.append(test[:])
# test[0] = 'Maria'
# test[1] = 22
# galera.append(test[:])
# print(galera)
# galera = [['João', 19, ], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# for p in galera:
#     print(f'\nOs nome da pessoas é, {p[0]}', end=' ')
#     print(f'e sua idade é {p[1]}', end='')
galera= []
dados = []
maior = menor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maiores, e {menor} menores de idade')