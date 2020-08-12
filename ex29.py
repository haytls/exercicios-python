#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrpassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ por cada km acima do limite.
v =int(input('Digite a velocidade: '))
if v>80:
    print('\033[31mVocê foi multado!\033[m')
    m = (v -80)*7
    print('\033[31mSua multa foi de R$ {:.2f}!\033[m'.format(m))
else:
    print('\033[32mEstá tudo Ok!\033[m')
