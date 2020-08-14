#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0:
#REPROVADO
# - Média entre 5.0 e 6.9:
#RECUPERAÇÃO
# - Média 7.0 ou superior:
#APROVADO
n1 = float(input('Primeiro nota: '))
n2 = float(input('Segunda nota: '))
media = float((n1+n2)/2)
if media >0  and media <5.0:
    print('\033[31mVocê foi reprovado!!\033[m')
elif media >= 5.0 and media <= 6.9:
    print("\033[34mVocê está de recuperação!!\033[m")
elif media >6.9 and media <10:
    print('\033[32mVocê foi aprovado, parabéns!!\033[m')
else:
    print('\033[4mA algum erro com a sua nota!!!\033[m')

