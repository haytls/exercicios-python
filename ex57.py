#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = 'F', 'M'
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo: ')).upper()
print('Então o seu sexo é {}'.format(s))
print('[F] = Feminino\n[M] = Masculino')
