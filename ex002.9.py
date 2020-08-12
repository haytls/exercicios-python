# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s =float(input('Digite o valor do salário R$:'))
print('O seu salário antigo era de \033[0;33mR$:{:.2f} reais\033[m, agora é de \033[0;33mR$:{:.2f} reais\033[m'.format(s, (s+(s*0.15))))

