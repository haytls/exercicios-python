numeros = [[], []]

for n in range(1, 8):
    c = int(input(f'Digite o {n}° valor: '))
    if c % 2 == 0:
        numeros[0].append(c)
    else:
        numeros[1].append(c)
numeros[1].sort()
print(f'Os números impares digitados foram: {numeros[1]}')
numeros[0].sort()
print(f'Os números pares digitados foram: {numeros[0]}')
