# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
a1 =str(input('Digite o nome do primeiro aluno: '))
a2 =str(input('Digite o nome do segundo aluno: '))
a3 =str(input('Digite o nome do terceiro aluno: '))
a4 =str(input('Digite o nome do terceiro aluno: '))
l =[a1, a2, a3, a4]
s = choice(l)
print('O aluno escolhido foi o(a) {} '.format(s))

