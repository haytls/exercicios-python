#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrpassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ por cada km acima do limite.
v =int(input('Digite a velocidade: '))
if v>80:
    print('Você foi multado!')
    m = (v -80)*7
    print('Sua multa foi de R$ {:.2f}!'.format(m))
else:
    print('Está tudo Ok!')
