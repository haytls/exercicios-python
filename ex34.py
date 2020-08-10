#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%
salario =float(input('Digite seu salário R$:'))
if salario > 1250:
    print('Com o aumento seu salário vai para R${:.2f}'.format((salario*0.10)+salario))
if salario <= 1250:
    print('Com o aumento seu salário vai para R${:.2f}'.format((salario*0.15)+salario))

