'''
Valores padrão para parâmetros
Ao definir uma função, os parâmetros pode
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será usado.
Refatorar: Editar o seu código.
'''
import os

def soma(x, y ,z=None):
  if z is not None:
    print(x + y + z)
  else:
    print(x + y)

os.system('cls')
soma(1, 2)
soma(3, 5)
soma(100, 200, 300)