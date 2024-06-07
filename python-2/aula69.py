'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
a palavra global faz uma variável do escopo externo ser a mesma do escopo interno.
'''
import os

x = 1

def escopo(): 

  global x # MÁ PRÁTICA
  x = 10

  def outra_funcao():
    global x # MÁ PRÁTICA
    x = 11
    y = 2
    print(x, y)

  outra_funcao()
  print(x)

os.system('cls')
escopo()