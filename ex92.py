#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de zero,
#o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
cartorio = {}
cartorio['Nome'] = str(input('Nome: '))
data = int(input('Ano de Nascimento: '))
ano = date.today().year - data
cartorio['Idade'] = ano
cartorio['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cartorio['ctps'] != 0:
    data1 = int(input('Ano de contratação: '))
    apos = (data1 - data) + 35
    cartorio['Contratação'] = data1
    cartorio['salário'] = int(input('Salário: R$ '))
    cartorio['Aposentadoria'] = apos
print('='*60)
print('=== RESULTADO ===')
print('='*60)
print(cartorio)
for k, v in cartorio.items():
    print(f'{k} tem o valor {v}')
