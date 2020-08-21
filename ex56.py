#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média da idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.
media = 0
maior = 0
quantas = 0
menor = 0
soma = 0
nomemais = ''
for pessoas in range(1,5):
    print('-----{}° Pessoa-----'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M][F]: ')).strip()
    media += idade / 4
    if pessoas == 1 and sexo in 'Mm':
        maior = idade
        nomemais = nome
    elif sexo in 'Mm' and idade > maior:
        maior = idade
        nomemais = nome
    if idade < 20 and sexo in'Ff':
        soma += 1
    menor = soma
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, nomemais))
print('Tem {} mulheres menores de 20 anos'.format(menor))


















