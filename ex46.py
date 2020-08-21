#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
# de artifício, de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('\033[1;31mContagem regressiva para o lançamento dos fogos\033[m')
sleep(1)
print('\033[32m*\033[m'*10)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[32m*\033[m'*10)
print('\033[1;31mOs fogos foram lançados!!\033[m')