'''
Lista de listas e seus índices
'''
import os

os.system('cls')
salas = [
    # 0           1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0        1         2
    ['Luiz', 'João', 'Eduarda',], # 2
]

# salas([linha][coluna])
print(salas[1][0])  
print(salas[2][2])
print(salas[0][1])

for sala in salas:
  print(sala) # printa as listas dentro de 'salas'

print('--------------------------------')

for sala in salas:
  print('A sala é:', sala)
  for aluno in sala:
    print(aluno)