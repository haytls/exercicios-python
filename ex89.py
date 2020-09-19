#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
#boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
ficha = []
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar ? ')).strip().upper()[0]
    if c == 'N':
        break
print('-='*30)
print(f'{"No.":<4}', f'{"NOME:<10"}', f'{"MÉDIA":>8.1f}')
print('-='*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('-='*30)
    p = int(input(f'Mostrar notas de qual aluno ? '))
    if p == 999:
        break
    if p <= len(ficha) -1:
        print(f'Notas de {ficha[p][0]} são {ficha[p][1]}')
print('FLW SEU BOSTAAAAAA')
















# while True:
#     temp.append(str(input('Nome: ')))
#     temp.append(float(input('Nota 1: ')))
#     temp.append(float(input('Nota 2: ')))
#     lista.append(temp)
#     temp.clear()
#     c = ' '
#     while c not in 'SN':
#         c = str(input('Deseja continuar ?')).strip().upper()[0]
#     if c == 'N':
#         break
# print(f'{"No. NOME"}', f'{"MÉDIA":>15}')
# for i, l in enumerate(lista):
#     print(f'{i}  {lista}')