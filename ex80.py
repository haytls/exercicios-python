#Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()).
#No final, mostre a lista ordenada na tela.
numeros = []
maior = menor = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
print(numeros)