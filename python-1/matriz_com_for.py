import os

os.system('cls')
matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

for lista in matriz:
    print('Linha:', lista)
    for valores in lista:
        print('Valor', valores)
    