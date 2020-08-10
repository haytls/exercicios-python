#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
frase =str(input('Digite o nome da cidade: ')).strip()
print(frase[:5].upper() == 'SANTO')

