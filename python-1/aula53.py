'''
enumerate = enumera iteráveis (índices)
'''
import os

os.system('cls')
#         [(0, 'Matheus'), (1, 'Arthur'), (3, 'Lucas'), (4, 'Iagor)]
lista = ['Matheus','Arthur','Lucas']
lista.append('Iagor')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
  print(item)

