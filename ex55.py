#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
ma = 0
me = 0
for c in range(1, 6):
    p = float(input("Digite o peso da {}° pessoa: ".format(c)))
    if c ==1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print('O maior peso lido foi de {}Kg'.format(ma))
print('O menor peso lido foi de {}Kg'.format(me))

