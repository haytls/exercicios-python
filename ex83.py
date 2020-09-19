#Crie um programa que o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parẽntesses abertos e fechados na ordem correta.
e = str(input('Digite uma expressão: '))
l = []
for s in e:
    if s == '(':
        l.append('(')
    elif s == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
