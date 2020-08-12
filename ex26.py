#Faça um programa queleia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A". Em que psoição ela aparece a primeira vez.
#Em que posição ela aparece a ultima vez.
frase =str(input('\033[30mDigite uma frase:\033[m ')).upper().strip()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.rfind('A')+1))



