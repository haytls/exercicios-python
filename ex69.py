#Crie eum programaque leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem 20 anos.
maioridade = 0
quantidadeh = 0
mulher20 = 0
print('-'* 30)
print('CADASTRE UMA PESSOA')
print('-'* 30)
while True:
    idade = int(input('Idade: '))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        print('-' * 30)
    continuar = " "
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        print('Fim do programa')
        break
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        quantidadeh += 1
    if sexo == 'M' and idade <= 20:
        mulher20 += 1
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {quantidadeh} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')
