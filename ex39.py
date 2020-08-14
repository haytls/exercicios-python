#Escreva um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda cai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
data = int(input('Ano em que você nasceu ? '))
atual = date.today().year
idade = atual - data
tf = 18 - idade
tp = idade - 18
datalist = atual + tf
datalist2 = atual - tp
print('Quem nasceu em {} tem {} anos em {}'.format(data, idade, atual))
if atual - data < 18:
    print("Faltam {} anos para seu alistamento.".format(tf))
    print("Seu alistamento será em {}".format(datalist))
elif idade ==18:
    print('Já está na hora de você se alistar!')
elif idade > 18:
    print('Você já passou {} anos do seu alistamento.'.format(tp))
    print('O ano que vocẽ devia ter se alistador era {}'.format(datalist2))

