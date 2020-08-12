# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1 =str(input('\033[4mO nome do primeiro aluno:\033[m '))
a2 =str(input('\033[4mO nome do segundo aluno:\033[m '))
a3 =str(input('\033[4mO nome do terceiro aluno:\033[m '))
a4 =str(input('\033[4mO nome do quarto aluno:\033[m '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação vai ser:')
print(lista)





