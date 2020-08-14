#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
preco = float(input('Qual é o preço do produto ? '))
cond = int(input("""Qual vai ser a forma de pagameto:
[1- À vista, dinheiro ou cheque ]
[2-       À vista no cartão     ]
[3-     Em até 2x no cartão     ]
[4-     3x ou mais no cartão    ]
Opção número ? """))
c1 = preco - (preco * 0.10)
c2 = preco - (preco * 0.05)
c3 = preco
c4 = (preco * 0.20) + preco
if cond == 1:
    print('O valor a ser pago é de {:.2f}'.format(c1))
elif cond == 2:
    print('O valor a ser pago é de {:.2f}'.format(c2))
elif cond == 3:
    print('O valor a ser pago é de {:.2f}'.format(c3))
elif cond == 4:
    print('O valor a ser pago é de {:.2f}'.format(c4))
else:
    print('Essa forma de pagamento não é aceita!!')

