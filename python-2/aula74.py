'''
Closure e funções que retornam outras funções
'''
# POSSO CRIAR FUNÇÕES QUE CRIAM OUTRAS FUNÇÕES
import os

def criar_saudacao(saudacao):
  def saudar (nome):
    return f'{saudacao}, {nome}!'
  return saudar

os.system('cls')
s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Bom noite')

print(s1('Matheus'))
print(s2('Matheus'))