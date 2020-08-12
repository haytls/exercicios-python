print("""Texto aqui""")
n1 =int(input('Digite um numero:'))
n2 =int(input('Digite outro:'))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('\033[34mA soma é {}\033[m, \033[33ma subitração é {}\033[m \033[32me a miltiplicação é {}\033[m'.format(s, su, m))
print('\033[35mA divisão é {:.2f}\033[m, \033[36ma divisão inteira é {}\033[m \033[30me a expodenciação é {}\033[m'.format(d, di, e))

