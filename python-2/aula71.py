'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''
# Lembre-se de desempacotamento
import os

os.system('cls')
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args): # 'args' empacota o que for enviado para a função dentro de um tupla
  total = 0
  for numero in args:
    total += numero
  return total

soma_1_2_3 = soma(1, 2, 3) # tupla
soma_4_5_6 = soma(4, 5, 6) # tupla

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros) # desempacota uma tupla para enviar como parâmetro para um função
print(outra_soma)

print(sum(numeros))