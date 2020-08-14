#A confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostrre sua categotia, de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Ate 20 anos: Sênior
# - Acima: Master
from datetime import date
ano = int(input('Em que ano você nasceu ?'))
atual = date.today().year
idade = int(atual - ano)
print(idade)
if idade >=1 and idade <= 9:
    print('Sua categoria é mirim')
elif idade > 9 and idade <= 14:
    print('Sua categoria é infantil')
elif idade > 14 and idade <= 19:
    print('Sua categoria é junior')
elif idade == 20:
    print('Sua categoria é sênior')
elif idade >20:
    print('Sua categoria é master')

