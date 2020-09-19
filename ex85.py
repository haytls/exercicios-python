#Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha
#separados os valores oares e ímpares. No final, mostre os valores pares e impares em ordem crescente.
lista = [[], []]
for n in range(1, 8):
    l = (int(input(f'Digite o {n}° número: ')))
    if l % 2 == 0:
        lista[0].append(l)
    elif l % 2 == 1:
        lista[1].append(l)
lista[1].sort()
print(f'Os valores ímpares digitados foram {lista[1]}')
lista[0].sort()
print(f'Os valores pares digitados foram {lista[0]}')