'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''
import os

def soma(x, y):
  # Definição
  return(x + y)

os.system('cls')
print(soma(1, 2)) # argumentos não nomeados, ordem importa
print(soma(y = 2, x = 1)) # argumentos nomeados, ordem não importa