#Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do
# comprador e em quanto anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exercer
#30% do salário ou então o empréstimo será negado.
valor =float(input('Qual o valor da casa: R$ '))
salario =float(input('Quanto você recebe: R$ '))
tempo =int(input('Em quantos anos você pretende pagar tudo ? '))
p = (valor/tempo)/12
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, tempo, p))
if p <=salario*0.30:
    print('\033[4mO seu emprestimo foi aprovado!\033[m')
elif p >salario*0.30:
    print('\033[31mSeu emprestimo não foi aceito, sinto muito.\033[m')
