'''
Dicionário em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor"
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int , float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves - {} - ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
'''

# EX: Para uma pessoa ou produto para cadastrar, precisa ter nome, sobrenome, id, CPF, etc. 
#   Podemos armazenar esses valores em uma única variável, a lista, mas a pesquisa de seus dados ficará difícil
#   Então nós usamos DICIONÁRIO
import os

os.system('cls')
pessoa = {
    'nome': 'Matheus',
    'sobrenome': 'Braga',
    'idade': 18,
    'altura': 1.85,
    'endereços': [
        {'rua': 'pinheiro machado', 'número': 260},
        {'rua': 'outra rua', 'número': 620}
    ],
} # dicionário

#print(pessoa)
print(pessoa['nome'])
print(pessoa['sobrenome'])
print('---------------------')
for chave in pessoa:
  print(chave,':',pessoa[chave])
print('---------------------')
# Manipulando chaves e valores em dicionários
jogo = {}

jogo['nome'] = 'Elden Ring' # chave recebe tal valor dentro de tal dicionário
print(jogo)
print(jogo['nome'])
print('---------------------')
pessoa_teste = {}

chave = 'nome'

pessoa_teste[chave] = 'Matheus'
pessoa_teste['sobrenome'] = 'Braga'

print(pessoa_teste[chave])

pessoa_teste[chave] = 'Maria'

#del pessoa_teste['sobrenome']
print(pessoa_teste)
print(pessoa_teste[chave])

# GET para ver se existe no dicionário
if pessoa_teste.get('sobrenome') is None:
  print('NÃO EXISTE CHAVE NO DICIONÁRIO')
else:
  print('EXISTE CHAVE NO DICIONÁRIO')

