# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1 =str(input('O nome do primeiro aluno: '))
a2 =str(input('O nome do segundo aluno: '))
a3 =str(input('O nome do terceiro aluno: '))
a4 =str(input('O nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação vai ser:')
print(lista)





