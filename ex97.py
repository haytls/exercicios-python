#Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#Ex:
#Escreva('Olá, Mundo!')
#Saída:
#-------------
 #Olá, Mundo!
#-------------
def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


escreva('Armano Barros')
escreva('Curso de Python no Youtube')
escreva('Cev')