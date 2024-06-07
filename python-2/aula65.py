'''
introdução a funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
'''
import os

def print_msg():
  print('Olá mundo')
  print('Meu nome é Matheus Braga')
  print('Eu estudo Programação')
  print()

def calculo_soma(a, b, c): # abc são os parâmetros que recebem argumentos
  print(a + b + c)

def calculo_soma_sem_argumentos(a=10, b=50, c=70): # abc são parâmetros mas podem ser tratados como variáveis
  print(a + b + c)

os.system('cls')
print_msg()
calculo_soma(5, 6, 9) # 5, 6 e 9 são argumentos enviados
calculo_soma(50, 60, 90)
calculo_soma(10, 20, 30)
calculo_soma_sem_argumentos()