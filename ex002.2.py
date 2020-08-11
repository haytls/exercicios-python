# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n =float(input('Digite um numero para iniciar:'))
print('O dobro é \033[1;32m{:.2f}\033[m '
      '\nO triplo é \033[1;32m{:.2f}\033[m '
      '\nE raiz quadrada é \033[1;32m{:.2f}\033[m'.format((n*2), (n*3), (n**(1/2))))

