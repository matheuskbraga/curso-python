'''
for in com listas
'''
import os

os.system('cls')
lista = ['Matheus', 'Arthur', 'Otávio']
lista.append('Marcelo')

indices = range(len(lista))

print(indices)

for nome in lista:
  print(nome, type(nome))

for indice in indices:
  print(indice, nome, type(nome))
