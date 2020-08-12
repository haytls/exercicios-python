# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
t = float(input('Digite uma temperatura:'))
print("A temperatura de \033[33m{:.1f}°C\033[m corresponde a \033[33m{:.1f}°F\033[m".format(t,((9*t)/5)+32))
