#Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
ano =int(input('Que ano quer analisar ? Coloque 0 se quiser analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100!=0 or ano % 400 == 0:
    print('\033[32mO ano de {} é bissexto\033[m'.format(ano))
else:
    print('\033[31mO ano de {} não é bissexto\033[m'.format(ano))

