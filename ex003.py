# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
t = float(input('Digite uma temperatura:'))
print("A temperatura de {:.1f}°C corresponde a {:.1f}°F".format(t,((9*t)/5)+32))
