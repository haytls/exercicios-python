# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
v =float(input('Digite um valor:'))
print('\033[1mO valor em centimetros é\033[m \033[4;34m{:.0f} cm\033[m,'
      ' \033[1mjá em milimetros é\033[m \033[4;34m{:.0f} mm\033[m'.format((v*10**2), (v*10**3)))

