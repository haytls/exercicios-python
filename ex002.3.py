# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.
n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
print('\033[1mA sua media é de\033[m \033[33m{:.1f}'.format((n1+n2)/2))
