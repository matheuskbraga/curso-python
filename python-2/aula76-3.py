import os

p1 = {
    'nome': 'Matheus',
    'sobrenome': 'Braga',
}

os.system('cls')

# Se EXISTIR a chave, printa o valor que tem esta chave
# Se NÃO EXISTIR a chave, printa o 'Não existe'
print(p1.get('nome', 'Não existe')) 

print('--------------------------')

# POP, retorna o valor da chave mas também a tira do dicionário
nome = p1.pop('nome')
print(nome)
print(p1)

print('--------------------------')

# POPITEM remove a última chave do meu dicionário
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

print('--------------------------')

p2 = {
  'nome': 'Matheus',
  'sobrenome': 'Braga',
  'idade': 21
}

# para atualizar os valores no dicionário
p2.update(nome='Arthur', sobrenome='Braguita', idade=18)
print(p2)
for chave in p2:
  print(p2[chave])