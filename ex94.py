#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade do grupo.
#C) Uma lista com todas as mulheres
#D) Uma lista com todas as pessoas com idade acima da média.
galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO! por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
media = soma / len(galera)
print('='*40)
print(f'A média de idades é de {media:5.2f} anos')
print(f'foram cadastrasdas {len(galera)} pessoas')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] > media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('ENCERRADO!!!')