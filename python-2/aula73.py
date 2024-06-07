'''
Higher Order Functions
Funções de primeira classe
'''
import os

def saudacao(msg):
  return msg

def executa(funcao, texto):
  return funcao(texto)

os.system('cls')
v = executa(saudacao, 'Bom dia')
print(v)