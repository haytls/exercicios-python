#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - escaleno: todos os lados diferentes
r1 = float(input('Primerio segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('\033[32mÉ possivel formar um triângulo\033[m')
else:
    print('\033[31mNão é possivel formar um triângulo\033[m')
if r1 == r2 and r1 == r3 and r2 == r3:
    print('\033[34mEssa formação é de um triângulo equilátero\033[m')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('\033[34mEsssa formação é de um triângulo isóceles\033[m')
else:
    print('\033[34mEssa formação contem todos os lados diferentes\033[m')