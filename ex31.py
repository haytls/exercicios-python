#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
#de até 200Km e R$0,45 para viagens mais longas.
distancia =float(input('Digite a distância percorrida: '))
if distancia<=200:
    v1= distancia*0.50
    print('O valor a ser pago é de R${:.2f}'.format(v1))
else:
    v2= distancia*0.45
    print('O valor a ser pago é de R${:.2f}'.format(v2))

