'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
'''
import os
import copy

os.system('cls')
d1 = {
    'nome': 'Matheus',
    'sobrenome': 'Braga',
    'idade': 21,
    'jogos': ['Elden Ring', 'Assassins Creed', 'GTA']
}

d2 = copy.deepcopy(d1) # deepcopy => cópia profunda, com isso podemos alterar subvalores (como listas) dentro dos dicionários

# valores alterados no dicionário deepcopy
d2['nome'] = 'Sócrates'
d2['jogos'][2] = 'Need for Speed Heat'

print(d1)
print(d2)