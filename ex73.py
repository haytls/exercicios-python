#Crie uma tupla preechida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#A) Apenas 5 primeiros
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time da Chapecoense.
lista = ('Vasco da Gama', 'Internacional', 'Atlético-MG', 'Bahia', 'Santos',
         'Atlético-PR', 'Grêmio', 'Botafogo', 'Palmeiras', 'Bragantino-SP',
         'Corinthians', 'Atlético-GO', 'São Paulo', 'Fluminense', 'Fortaleza',
         'Sport Recife', 'Flamengo', 'Goiás', 'Ceará SC', 'Coritiba')
cont = 0
cont += 1
print(f'Lista de times do Brasileirão: {lista}')
print(f'Os 5 primeiros São: {lista[:5]}')
print(f'Os 4 últimos são: {lista[16:]}')
print(f'Times em ordem alfabetica: {sorted(lista)}')
print(f'O Flamengo eatá na {lista.index("Flamengo")+1}° posição')
