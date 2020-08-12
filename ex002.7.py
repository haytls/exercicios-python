# Faç um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade necessária
# para pintá-la, sabendo que casa litro de tinta pinta uma área de 2m².
a =int(input('Altura:'))
l =int(input('Largura:'))
print('Á área da parede é de \033[1;35m{:.2f} metros\033[m, '
      'a quantidade de tinta necessaria pra pintar é '
      'de \033[1;35m{:.2f} litros\033[m'.format((a*l), ((a*l)/2)))

