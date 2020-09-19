# def men(msg):
#     print('='*40)
#     print(msg)
#     print('='*40)
# men(f'{"SISTEMA E ALUNOS":^40}')
# men(f'{"CADASTRO DE RESIDENTES":^40}')
# men(f'{"AQUI É XANDÃO, SEGURA!":^40}')
# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')
#     print()
#
#
#
# soma(4, 5)
# soma(8, 9)
# soma(2, 1)
def contador(*núm):
    for valor in núm:
        print(f'{valor} ', end='')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


# def dobrar(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
#
#
# valores = [7, 2, 5, 0, 4]
# dobrar(valores)
# print(valores)