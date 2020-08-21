#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
cont = 0
s = 0
n = 0
while True:
    n = int(input('Digite um valor (99 faz parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'A quantidade de números digitados foi de {cont} e a soma entre eles é de {s}')