#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input('Nome: ')).strip()
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperaçãoo'
else:
    aluno['situação'] = 'Reprovado'
for v, c in aluno.items():
    print(f'{v} é igual a {c}')