#Crie um programa que leia o ano de nascimento de sete pessoas.
#no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
pme = 0
pma = 0
h = date.today().year
for c in range(7):
    n = int(input('Digite o ano de nascimento de uma pessoa: '))
    if h - n < 21:
        pme = pme + 1
    elif h - n >= 21:
        pma = pma + 1
print('{} pessoas não são maiores de idade ainda.'.format(pme))
print('{} pessoas são maiores de idade'.format(pma))
