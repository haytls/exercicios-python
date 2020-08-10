# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
v =float(input('Digite um valor:'))
print('O valor em centimetros é {:.2f}, já em milimetros é {:.2f}'.format((v*10**2), (v*10**3)))

