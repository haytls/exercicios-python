# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
d =int(input('Quantos dias foram alugados ? '))
k =float(input('Quantos km rodados ? '))
print('O total a pagar é R${:.2f}'.format((60*d) + (0.15*k)))

