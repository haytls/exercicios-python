# dados = {'nome':'pedro', 'idade': 25}
# dados['sexo'] = 'M'
# print(dados['idade'], dados['nome'], dados['sexo'])
# filme = {'titulo': 'Star Wars',
#          'ano': 1977,
#          'diretor': 'George Lucas'
# }
# for k, v in filme.items():
#     print(f'O {k} é {v}')
# pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'idade': 22}
# # print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# # print(pessoas.items())
# pessoas['peso'] = 98.5
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(brasil[0]['uf'])
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O {k} do {v} ')