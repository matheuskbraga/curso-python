'''
Retorno de valores das funções (return)
'''
import os

def soma (x, y):
  return x + y

def multiplicacao(num_repeticao_desejado):
  lista_valores = []
  for repete in range(num_repeticao_desejado):
    lista_valores.append((repete + 1) * 10)
  return lista_valores

os.system('cls')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)
print('----------------')
num_repeticao_desejado = 10
print(multiplicacao(num_repeticao_desejado))