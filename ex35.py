#Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
print(20* '-=')
print('Analizador de Triãngulos')
print(20* '-=')
c1 = float(input('Primeiro segmento: '))
c2 = float(input('Segundo segmento: '))
c3 = float(input('Terceiro segmento: '))
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 +c2:
    print('\033[32mOs segmentos acima podem formar triângulos\033[m')
else:
    print('\033[31mOs segmantos acima não podem formar triângulos\033[m')

